from . import forms
import math
import copy


class InvalidKeys(Exception):
        """Exception raised for InvalidKeys scenarios.

        Attributes:
            message -- explanation of the error
        """

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

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


def calculate_convergence(tables_data: dict) -> list:
        """
        The first element of the list is the value of matrix table A,
        the second element of the list is the value of matrix table B
        """
        table_indexes = []
        form_data = {}
        rows_table_1 = []
        rows_table_2 = []
        c = 0
        for k, v in tables_data.items():
            if k[5:7] not in table_indexes:
                c += 1
                table_indexes.append(k[5:7])
            if c == 1:
                if k[8:11] not in rows_table_1:
                    rows_table_1.append(k[8:11])
                if form_data.get(str(table_indexes[0])) is None:
                    form_data[str(table_indexes[0])] = {}
                if form_data[str(table_indexes[0])].get(k[8:11]) is None:
                    form_data[str(table_indexes[0])][k[8:11]] = []
                form_data[str(table_indexes[0])][k[8:11]].append(v)
            elif c == 2:
                if k[8:11] not in rows_table_2:
                    rows_table_2.append(k[8:11])
                if form_data.get(str(table_indexes[1])) is None:
                    form_data[str(table_indexes[1])] = {}
                if form_data[str(table_indexes[1])].get(k[8:11]) is None:
                    form_data[str(table_indexes[1])][k[8:11]] = []
                form_data[str(table_indexes[1])][k[8:11]].append(v)


        row_values = []
        for row in rows_table_1:
            row_abs = []
            for i in form_data[table_indexes[0]][row]:
                row_abs.append(abs(float(i)))
            row_values.append(max(row_abs))
            
        row_values2 = []
        for row in rows_table_2:
            row_abs = []
            for i in form_data[table_indexes[1]][row]:
                row_abs.append(abs(float(i)))
            row_values2.append(max(row_abs))

        return [max(row_values), max(row_values2)]


def calculate_k(a:float, b:float):
    print(a, "calculate_k B")
    equation = (math.log10(0.001) + math.log10(1-a) - math.log10(b))/math.log10(a)
    return equation



def collect_data_from_matrix_tables(tables_data: dict) -> list:
        """
        returns the array, where the first element is the dict of elements from matrix A,
        the second element is the dict of elements from matrix B.
        """
        table_indexes = []
        form_data = {}
        c = 0
        
        for k, v in tables_data.items():
            if k[5:7] not in table_indexes:
                c += 1
                table_indexes.append(k[5:7])
            if c == 1:
                if form_data.get(str(table_indexes[0])) is None:
                    form_data[str(table_indexes[0])] = {}
                if form_data[str(table_indexes[0])].get(k[8:12]) is None:
                    form_data[str(table_indexes[0])][k[8:12]] = []
                form_data[str(table_indexes[0])][k[8:12]].append(v)
            elif c == 2:
                if form_data.get(str(table_indexes[1])) is None:
                    form_data[str(table_indexes[1])] = {}
                if form_data[str(table_indexes[1])].get(k[8:12]) is None:
                    form_data[str(table_indexes[1])][k[8:12]] = []
                form_data[str(table_indexes[1])][k[8:12]].append(v)
        return [form_data[str(table_indexes[0])], form_data[str(table_indexes[1])]]


def calculate_iteration(matrix_A: dict, matrix_B: dict, k_index: int=0) -> dict:
         """
         expects the matrix elements in the format as matrix has tableXX, that has row1, row2, row3, .., rown
         """
         table = {}
         i = 0
         x_amount =  len(matrix_B.keys())
         print(matrix_A, matrix_B)
         for k in matrix_A.keys():
            if not matrix_A.get(k):
                raise InvalidKeys(message="matrix_A is broken")
         if x_amount == 2:  
             table_row = {"x1": {}, "x2": {}}
         elif x_amount == 3:
             table_row = {"x1": {}, "x2": {}, "x3": {}}
         elif x_amount == 4:
             table_row = {"x1": {}, "x2": {}, "x3": {}, "x4": {}}
         elif x_amount == 5:
             table_row = {"x1": {}, "x2": {}, "x3": {}, "x4": {}, "x5": {}}
         while i < k_index: 
             table_row_copy = copy.deepcopy(table_row)
             c = 0
             for r in table_row_copy.keys():
                 res = 0 
                 if i == 0:
                     c += 1
                     for k in matrix_B.keys():
                         if str(c) in r and str(c) in k:

                            table_row_copy[r] = matrix_B[k][0]

                     continue
                 for k in matrix_A.keys(): 
                     for v in matrix_A[k]:
                          if table_row_copy.get(r):
                              res += v * table_row_copy[r]
                          else:
                              res += v * matrix_B[k][0]
                 table_row_copy[r] = res
             table[str(i)] = table_row_copy

             i += 1
         elements_in_row = []
         elements_in_row2 = []
         c = 0
         for index, table_row in table.items():
             table_row_copy = copy.deepcopy(table_row)
             for value in table_row_copy.values():
                 if len(elements_in_row) >= x_amount:
                     elements_in_row2.append(value)
                 else:
                     elements_in_row.append(value)
             if c == 0:
                 table_row_copy["delta"] = "-"
             if c > 0:
                table_row_copy["delta"] = abs(max(elements_in_row2)-max(elements_in_row)) 
                elements_in_row = elements_in_row2
                elements_in_row2 = []
             table_row_copy["k"] = c
             table_row_copy["row_index"] = c + 2
             table[index] = table_row_copy
             c += 1

         return table
           

