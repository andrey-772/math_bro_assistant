from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import json
from . import business_logic

def main_page(request):
    del request.session
    context = {"row1": 3, "column1": 3, "row2": 3, "column2": 1}
    return render(request, "base.html", {"context": context})


@csrf_exempt
def generate_matrix_table(request):
    if request.method == "POST":
        context = {}
        data = json.loads(request.body)
        form1_obj = business_logic.get_the_form(str(int(data.get("row1")))+str(int(data.get("column1"))))
        form2_obj = business_logic.get_the_form(str(int(data.get("row2")))+str(int(data.get("column2"))))
        form1 = form1_obj()
        form2 = form2_obj()
        context["row1"] = int(data.get("row1"))
        context["column1"] = int(data.get("column1"))
        context["row2"] = int(data.get("row2"))
        context["column2"] = int(data.get("column2"))
        request.session["context"] = context
        print("context", context)
        print('return render(request, "base-matrix-table.html", {"context": context, "form1": form1, "form2": form2})')
        return render(request, "base-matrix-table.html", {"context": context, "form1": form1, "form2": form2})
    raise Http404


@csrf_exempt
def simple_iteration_method(request):
    form_data_not_modified = request.POST
    form_data_modified = {}
    table_indexes = []
    form_data_for_first_table = {}
    form_data_for_second_table = {}
    request.session["matrix_fields"] = {}
    request.session["matrix_fields_modified"] = {}
    for field_name, field_value in form_data_not_modified.items():
        m_field_name = ""
        for s in field_name:
             if s == "-":
                 m_field_name += "_"
             else:
                 m_field_name += s
        try:
            form_data_modified[m_field_name] = float(field_value)
        except ValueError:
            if "," in field_value:
                new_field_value = ""
                for s in field_value:
                    if s == ",":
                        new_field_value += "."
                        continue
                    new_field_value += s
                form_data_modified[m_field_name] = float(new_field_value) 
        request.session["matrix_fields"][field_name] = field_value    
    request.session["matrix_fields_modified"] = form_data_modified
    c = 0
    for k, v in form_data_modified.items():
        if k[5:7] not in table_indexes:
            c += 1
            table_indexes.append(k[5:7])
        if c == 1:
            form_data_for_first_table[k[8:]] = v
        elif c == 2:
            form_data_for_second_table[k[8:]] = v
    form_class1 = business_logic.get_the_form(table_index=table_indexes[0])
    form_class2 = business_logic.get_the_form(table_index=table_indexes[1])
    form1 = form_class1(form_data_for_first_table)
    form2 = form_class2(form_data_for_second_table)
    request.session["form1_index"] = table_indexes[0]
    request.session["form2_index"] = table_indexes[1]
    if form1.is_valid() and form2.is_valid():    
        return redirect("/solve_by_simple_iteration_method/")
    

def solve_by_simple_iteration_method(request):
    request.session["first_step"] = {}
    request.session["second_step"] = {}
    form1_obj = business_logic.get_the_form(request.session.get("form1_index"))
    form2_obj = business_logic.get_the_form(request.session.get("form2_index"))
    form1 = form1_obj()
    form2 = form2_obj()
    request.session["first_step"]["a"], request.session["first_step"]["b"] = business_logic.calculate_convergence(tables_data=request.session.get("matrix_fields_modified")) 
    if request.session["first_step"]["a"] < 1:  
        request.session["first_step"]["operator"] = "<"
        request.session["first_step"]["message"] = "System is convergent"
        if request.session["first_step"]["b"] != 0 and request.session["first_step"]["a"] != 0:
            k=business_logic.calculate_k(a=request.session["first_step"]["a"],b=request.session["first_step"]["b"]) 
            request.session["second_step"]["k1"] = round(k, 3)
            request.session["second_step"]["k2"] = int(k)
            request.session["second_step"]["columns_n"] = int(k)

            data = business_logic.collect_data_from_matrix_tables(tables_data=request.session.get("matrix_fields_modified"))
            table_data = business_logic.calculate_iteration(matrix_A=data[0], matrix_B=data[1], k_index=request.session["second_step"]["k2"])
            request.session["second_step"]["table"] = table_data
    elif request.session["first_step"]["a"] > 1:
        request.session["first_step"]["operator"] = ">"
        request.session["first_step"]["message"] = "System is not convergent"
    else:
        request.session["first_step"]["operator"] = "="
        request.session["first_step"]["message"] = "System is not convergent"    
    return render(request, "simple_iteration_method.html", context={"context": request.session.get("context"), "matrix_fields": request.session.get("matrix_fields"), "form1": form1, "form2": form2, "first_step": request.session["first_step"], "second_step": request.session["second_step"]})


