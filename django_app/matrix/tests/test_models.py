from matrix.models import MatrixTable
from django.test import TestCase



class MartixTableModelTest(TestCase):
    def test_default_values(self):
        matrix_table = MatrixTable()
        self.assertEqual(matrix_table.row1, "3") 
        self.assertEqual(matrix_table.column1, "3") 
        self.assertEqual(matrix_table.row2, "3") 
        self.assertEqual(matrix_table.column2, "1")


