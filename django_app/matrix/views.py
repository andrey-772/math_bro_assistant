from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MatrixTable

# Create your views here.
def main_page(request):
    return render(request, "base.html")


@csrf_exempt
def matrix_table(request):
    context = {"row1": 3, "column1": 3, "row2": 3, "column2": 1}
    if request.method == "POST":
        data = json.loads(request.body)
        context["row1"] = int(data.get("row1"))
        context["column1"] = int(data.get("column1"))
        context["row2"] = int(data.get("row2"))
        context["column2"] = int(data.get("column2"))
        MatrixTable.objects.create(row1=context["row1"], column1=context["column1"], row2=context["row2"], column2=context["column2"])
    return render(request, "base-matrix-table.html", context)