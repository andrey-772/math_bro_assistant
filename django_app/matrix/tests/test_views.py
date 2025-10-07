from django.test import TestCase
from matrix.models import MatrixTable


class MainPageTest(TestCase):
     def test_main_page_uses_base_template(self):
         response = self.client.get("/")
         self.assertTemplateUsed(response, "base.html")


     def test_generate_matrix_table_works(self):
         response = self.client.get("/generate_table/")
         self.assertTemplateUsed(response, "base-matrix-table.html")

         
     
