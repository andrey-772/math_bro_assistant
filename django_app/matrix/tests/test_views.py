from django.test import TestCase
from matrix import forms
from django.contrib.sessions.backends.db import SessionStore
import json


class MainPageTest(TestCase):
    def test_uses_right_template(self):
         response = self.client.get("/")
         self.assertTemplateUsed(response, "base.html")


class MatrixTableTest(TestCase):
    def test_uses_right_templates(self):
         data = {"row1": 3, "column1": 3, "row2": 3, "column2": 1}
         response = self.client.post("/generate_table/", content_type="application/json", data=json.dumps(data))
         self.assertTemplateUsed(response, "base-matrix-table.html")
         self.client.get("/generate_table/")
         

class SimpleIterationMethodTest(TestCase):
    def test_uses_render_when_form_data_is_valid_default(self):
        self.__create_and_fill_client_session()
        for item_n in (2, 3, 4, 5):
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", blank=True)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", blank=True)
            dataset.update(dataset2)
            response = self.client.post("/simple_iteration_method/", data=dataset)
            self.assertRedirects(response, "/solve_by_simple_iteration_method/")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=True)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", blank=True)
                dataset.update(dataset2)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.assertRedirects(response, "/solve_by_simple_iteration_method/")
                

    def test_uses_redirect_when_form_data_is_valid(self):
        self.__create_and_fill_client_session()
        for item_n in (2, 3, 4, 5):
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", blank=False)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", blank=False)
            dataset.update(dataset2)
            response = self.client.post("/simple_iteration_method/", data=dataset)
            self.assertRedirects(response, "/solve_by_simple_iteration_method/")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=False)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", blank=False)
                dataset.update(dataset2)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.assertRedirects(response, "/solve_by_simple_iteration_method/")


    def __create_and_fill_client_session(self):
        data_set = self.__get_dataset(table_index="33")
        data_set2 = self.__get_dataset(table_index="31")
        data_set.update(data_set2)
        ss = self.client.session
        ss["form1_index"] = "33" 
        ss["form2_index"] = "31"
        ss["context"] = {"row1": "3", "column1": "3", "row2": "3", "column2": "1"}
        ss["matrix_fields_modified"] = data_set
        ss["matrix_fields"] = data_set
        ss["first_step"] = {}
        ss["first_step"]["a"] = 0
        ss["first_step"]["b"] = 0
        ss["first_step"]["operator"] = "<"
        ss.save()


    def __get_dataset(self, table_index: str, blank: bool=False) -> dict:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))

                   
        data = {}   
        if blank:
            value = 0
        else:
            value = 123.1
        for k in dataset_keys_list:
            data[k] = value
        return data

         
     


class SolveBySimpleIterationMethodTest(TestCase):
    def test_renders_right_template(self):
        self.__create_and_fill_client_session()
        response = self.client.get("/solve_by_simple_iteration_method/")
        self.assertTemplateUsed(response, "simple_iteration_method.html") 


    def test_render_with_right_context(self):
        self.__create_and_fill_client_session()
        print("123")
        response = self.client.get("/solve_by_simple_iteration_method/")
        for i in ("context", "matrix_fields", "form1", "form2"):
            self.assertIn(i, response.context)
        for i in response.context["context"].values():
            self.assertIn(int(i), (1, 2, 3, 4))
        for i in response.context["context"].keys():
            self.assertIn(i, ("row1", "row2", "column1", "column2"))
        for i in response.context["matrix_fields"].values():
            self.assertNotEqual(i, "")
        self.assertIsInstance(response.context["form1"], self.__get_the_form(table_index=f"{response.context['context']['row1']}{response.context['context']['column1']}"))
        self.assertIsInstance(response.context["form2"], self.__get_the_form(table_index=f"{response.context['context']['row2']}{response.context['context']['column2']}"))
        self.assertIsInstance(response.context["first_step"]["a"], float)
        self.assertIn(response.context["first_step"]["operator"], ["<", ">", "="])
        

    def __create_and_fill_client_session(self):
        data_set = self.__get_dataset(table_index="33")
        data_set2 = self.__get_dataset(table_index="31")
        data_set.update(data_set2)
        ss = self.client.session
        ss["form1_index"] = "33" 
        ss["form2_index"] = "31"
        ss["context"] = {"row1": "3", "column1": "3", "row2": "3", "column2": "1"}
        ss["matrix_fields"] = data_set
        ss["matrix_fields_modified"] = data_set
        ss["first_step"] = {}
        ss["first_step"]["a"] = 0
        ss["first_step"]["b"] = 0
        ss["first_step"]["operator"] = "<"
        ss.save()


    def __get_the_form(self, table_index: str):
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


    def __get_dataset(self, table_index: str, blank: bool=False) -> dict:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))

                   
        data = {}   
        if blank:
            value = 0
        else:
            value = 123.1
        for k in dataset_keys_list:
            data[k] = value
        return data

         
     
