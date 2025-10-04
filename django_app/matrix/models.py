from django.db import models


class MatrixTable(models.Model):
    row1 = models.CharField(default="3")
    column1 = models.CharField(default="3")
    row2 = models.CharField(default="3")
    column2 = models.CharField(default="1")
