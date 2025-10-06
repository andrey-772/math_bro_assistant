from matrix.models import MatrixTable
from django.test import TestCase



class MartixTableModelTest(TestCase):
    def test_default_values(self):
        matrix_table = MatrixTable()
        for field in MatrixTable._meta.fields:
            if field.name == "id":
                continue
            value = getattr(matrix_table, field.name)
            self.assertEqual(value, 0)



