from django.test import TestCase
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
    def dtest_uses_render_when_form_data_is_valid_default(self):
        for item_n in (2, 3, 4, 5):
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", blank=True)
            response = self.client.post("/simple_iteration_method/", data=dataset)
            self.assertTemplateNotUsed(response, "base-matrix-table.html")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=True)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.assertNotTemplateUsed(response, "base-matrix-table.html")
                

    def test_uses_redirect_when_form_data_is_valid(self):
        for item_n in (2, 3, 4, 5):
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", blank=False)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", blank=False)
            print("dataset", type(dataset), dataset)
            dataset.update(dataset2)
            response = self.client.post("/simple_iteration_method/", data=dataset)
            self.assertRedirects(response, "/solve_by_simple_iteration_method/")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=False)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", blank=False)
                dataset.update(dataset2)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.assertRedirects(response, "/solve_by_simple_iteration_method/")

        



    def __get_dataset(self, table_index: str, blank: bool=False) -> dict:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))

                   
        data = {}   
        if blank:
            value = ""
        else:
            value = 123.1
        for k in dataset_keys_list:
            data[k] = value
        return data




     

         
     
