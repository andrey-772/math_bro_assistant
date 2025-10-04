from django.test import TestCase
from matrix.models import MatrixTable


class MainPageTest(TestCase):
     def test_main_page_uses_base_template(self):
         response = self.client.get("/")
         self.assertTemplateUsed(response, "base.html")


     def test_generate_matrix_table_works(self):
         response = self.client.get("/generate_table/")
         self.assertTemplateUsed(response, "base-matrix-table.html")


     def test_can_save_a_POST_request_to_existing_table(self):
         MatrixTable.objects.create()
         self.client.post("generate_table/", {
                "row1": "1",
                "column1": "1",
                "row2": "1",
                "column2": "1"
             }
         )

         self.assertEqual(MatrixTable.objects.count(), 1)

         
     
