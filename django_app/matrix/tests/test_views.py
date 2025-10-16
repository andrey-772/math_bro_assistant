from django.test import TestCase
import json
from . import test_views_additional_logic



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
            self.__create_and_fill_client_session()    
            self.assertRedirects(response, "/solve_by_simple_iteration_method/")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=True)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", blank=True)
                dataset.update(dataset2)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.__create_and_fill_client_session()
                self.assertRedirects(response, "/solve_by_simple_iteration_method/")
                

    def test_uses_redirect_when_form_data_is_valid(self):
        for item_n in (2, 3, 4, 5):
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", blank=False)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", blank=False)
            dataset.update(dataset2)
            response = self.client.post("/simple_iteration_method/", data=dataset)
            self.__create_and_fill_client_session()
            self.assertRedirects(response, "/solve_by_simple_iteration_method/")
            if item_n < 5:
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", blank=False)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", blank=False)
                dataset.update(dataset2)
                response = self.client.post("/simple_iteration_method/", data=dataset)
                self.__create_and_fill_client_session()
                self.assertRedirects(response, "/solve_by_simple_iteration_method/")


    def __create_and_fill_client_session(self):
        data_set = self.__get_dataset(table_index="33", for_method=False)
        data_set2 = self.__get_dataset(table_index="31")
        data_set.update(data_set2)
        ss = self.client.session
        ss["form1_index"] = "33" 
        ss["form2_index"] = "31"
        ss["context"] = {"row1": "3", "column1": "3", "row2": "3", "column2": "1"}
        ss["matrix_fields"] = data_set
        ss["matrix_fields_modified"] = data_set
        ss.save()

    
    def __get_dataset(self, table_index: str, blank: bool=False, for_method: bool=False) -> dict:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))

                   
        data = {}   
        if blank:
            value = 0
        elif for_method:
            value = 0.5
        else:
            value = 123.1
        for k in dataset_keys_list:
            data[k] = value
        return data


class SolveBySimpleIterationMethodTest(TestCase):
    def setUp(self):
        self.solveBySimpleIterationMethod = test_views_additional_logic.SolveBySimpleIterationMethod()
        data_set = self.solveBySimpleIterationMethod.get_dataset(table_index="33")
        data_set2 = self.solveBySimpleIterationMethod.get_dataset(table_index="31")
        data_set.update(data_set2)
        self.__create_and_fill_client_session(data_set)
        self.response = self.client.get("/solve_by_simple_iteration_method/")
        

    def test_renders_right_template(self):
        response = self.client.get("/solve_by_simple_iteration_method/")
        self.assertTemplateUsed(response, "simple_iteration_method.html") 


    def test_returns_all_end_points(self):
        for i in ("context", "matrix_fields", "form1", "form2", "first_step", "second_step"):
            self.assertIn(i, self.response.context)


    def test_calculate_convergence_business_logic(self):
        self.assertIsInstance(self.response.context["first_step"]["a"], float)
        self.assertIsInstance(self.response.context["first_step"]["b"], float)
        self.assertIsInstance(self.response.context["first_step"]["message"], str)
                
        data_set = self.solveBySimpleIterationMethod.get_dataset(table_index="33", blank=True)
        data_set2 = self.solveBySimpleIterationMethod.get_dataset(table_index="31", blank=True)
        data_set.update(data_set2)
        self.__create_and_fill_client_session(data_set)
        response = self.client.get("/solve_by_simple_iteration_method/")
        self.assertEqual(response.context["first_step"]["operator"], "<")
        self.assertEqual(response.context["first_step"]["message"], "System is convergent")


        data_set = self.solveBySimpleIterationMethod.get_dataset(table_index="33", is_1=True)
        data_set2 = self.solveBySimpleIterationMethod.get_dataset(table_index="31", is_1=True)
        data_set.update(data_set2)
        self.__create_and_fill_client_session(data_set)
        response = self.client.get("/solve_by_simple_iteration_method/")
        self.assertEqual(response.context["first_step"]["operator"], "=")
        self.assertEqual(response.context["first_step"]["message"], "System is not convergent")


        data_set = self.solveBySimpleIterationMethod.get_dataset(table_index="33")
        data_set2 = self.solveBySimpleIterationMethod.get_dataset(table_index="31")
        data_set.update(data_set2)
        self.__create_and_fill_client_session(data_set)
        response = self.client.get("/solve_by_simple_iteration_method/")
        self.assertEqual(response.context["first_step"]["operator"], ">")
        self.assertEqual(response.context["first_step"]["message"], "System is not convergent")


    def test_forms_are_fine(self):
        self.assertIsInstance(self.response.context["form1"], self.solveBySimpleIterationMethod.get_the_form(table_index=f"{self.response.context['context']['row1']}{self.response.context['context']['column1']}"))
        self.assertIsInstance(self.response.context["form2"], self.solveBySimpleIterationMethod.get_the_form(table_index=f"{self.response.context['context']['row2']}{self.response.context['context']['column2']}"))


    def test_business_logic_iteration_part(self):
        data_set = self.solveBySimpleIterationMethod.get_dataset(table_index="33", for_method=True)
        data_set2 = self.solveBySimpleIterationMethod.get_dataset(table_index="31", for_method=True)
        data_set.update(data_set2)
        self.__create_and_fill_client_session(data_set)
        response = self.client.get("/solve_by_simple_iteration_method/")


        self.assertIsInstance(response.context["second_step"]["k1"], float)
        self.assertIsInstance(response.context["second_step"]["k2"], int)

        data = self.solveBySimpleIterationMethod.collect_data_from_matrix_tables(tables_data=data_set)

        table_data = self.solveBySimpleIterationMethod.calculate_iteration(matrix_A=data[0], matrix_B=data[1], k_index=int(response.context["second_step"]["k2"]))
        print(table_data, " data __collect_data_from_matrix_tables")
        self.assertEqual(len(response.context["second_step"]["table"]), response.context["second_step"]["k2"])
        self.assertIn(len(response.context["second_step"]["rows_amount"], [2, 3, 4, 5]))
        for k1 in response.context["second_step"]["table"].keys():
            self.assertIsInstance(int(k1), int)
            for k2 in response.context["second_step"]["table"][k1].keys():
                self.assertIn(k2, ["x1", "x2", "x3", "x4", "x5", "delta"])
                self.assertIsInstance(response.context["second_step"]["table"][k1][k2], float)
                self.assertEqual(response.context["second_step"]["table"][k1][k2], table_data[k1][k2])


    def __create_and_fill_client_session(self, data_set: dict):
        ss = self.client.session
        ss["form1_index"] = "33" 
        ss["form2_index"] = "31"
        ss["context"] = {"row1": "3", "column1": "3", "row2": "3", "column2": "1"}
        ss["matrix_fields"] = data_set
        ss["matrix_fields_modified"] = data_set
        ss.save()


    
         
     
