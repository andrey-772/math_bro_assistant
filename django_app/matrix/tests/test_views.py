from django.test import TestCase


class MainPageTest(TestCase):
     def test_uses_right_template(self):
         response = self.client.get("/")
         self.assertTemplateUsed(response, "base.html")


class MatrixTableTest(TestCase):
     def test_uses_right_template(self):
         response = self.client.get("/generate_table/")
         self.assertTemplateUsed(response, "base-matrix-table.html")


class SimpleIterationMethodTest(TestCase):
     def test_uses_right_template(self):
         response = self.client.get("/solve_matrix_system_by_simple_iteration_method/")
         self.assertTemplateUsed(response, "simple_iteration_method.html")


     

         
     
