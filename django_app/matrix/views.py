from urllib import response
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import json
from . import forms


def get_the_form(table_index: str):
    if table_index == "21":
        return forms.Table21
    if table_index == "22":
        return forms.Table22
    if table_index == "23":
        return forms.Table23
    if table_index == "24":
        return forms.Table24
    if table_index == "25":
        return forms.Table25
    if table_index == "31":
        return forms.Table31
    if table_index == "32":
        return forms.Table32
    if table_index == "33":
        return forms.Table33
    if table_index == "34":
        return forms.Table34
    if table_index == "35":
        return forms.Table35
    if table_index == "41":
        return forms.Table41
    if table_index == "42":
        return forms.Table42
    if table_index == "43":
        return forms.Table43
    if table_index == "44":
        return forms.Table44
    if table_index == "45":
        return forms.Table45
    if table_index == "51":
        return forms.Table51
    if table_index == "52":
        return forms.Table52
    if table_index == "53":
        return forms.Table53
    if table_index == "54":
        return forms.Table54
    if table_index == "55":
        return forms.Table55

def main_page(request):
    del request.session
    context = {"row1": 3, "column1": 3, "row2": 3, "column2": 1}
    return render(request, "base.html", {"context": context})


@csrf_exempt
def generate_matrix_table(request):
    if request.method == "POST":
        context = {}
        data = json.loads(request.body)
        form1_obj = get_the_form(str(int(data.get("row1")))+str(int(data.get("column1"))))
        form2_obj = get_the_form(str(int(data.get("row2")))+str(int(data.get("column2"))))
        form1 = form1_obj()
        form2 = form2_obj()
        context["row1"] = int(data.get("row1"))
        context["column1"] = int(data.get("column1"))
        context["row2"] = int(data.get("row2"))
        context["column2"] = int(data.get("column2"))
        request.session["context"] = context
        print("context", context)
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
    c = 0
    for k, v in form_data_modified.items():
        print(f"k- {k}, v- {v}, index- {k[5:7]}")
        if k[5:7] not in table_indexes:
            c += 1
            table_indexes.append(k[5:7])
        if c == 1:
            form_data_for_first_table[k[8:]] = v
        elif c == 2:
            form_data_for_second_table[k[8:]] = v
    form_class1 = get_the_form(table_index=table_indexes[0])
    form_class2 = get_the_form(table_index=table_indexes[1])
    form1 = form_class1(form_data_for_first_table)
    form2 = form_class2(form_data_for_second_table)
    request.session["form1_index"] = table_indexes[0]
    request.session["form2_index"] = table_indexes[1]
    if form1.is_valid() and form2.is_valid():    
        return redirect("/solve_by_simple_iteration_method/")
    

def solve_by_simple_iteration_method(request):
    return render(request, "base.html")