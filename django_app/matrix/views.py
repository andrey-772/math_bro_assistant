from django.shortcuts import render
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
def matrix_table(request):
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
