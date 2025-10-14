from django.test import TestCase
from matrix import models

from matrix import forms


class MatrixTablesFormTest(TestCase):
    def __get_dataset(self, table_index: str, blank: bool=False) -> dict:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("row"+str(row_index)+"_column"+str(column_index))

                   
        data = {}   
        if blank:
            value = ""
        else:
            value = 123.1
        for k in dataset_keys_list:
            data[k] = value
        return data


    def __test_form_dont_validates_blank_items_logic(self, form_obj, table_index):
        form = form_obj(self.__get_dataset(table_index=table_index, blank=True))
        self.assertFalse(form.is_valid())


    def __test_form_save_logic(self, table_obj, form_obj, table_index):
        form = form_obj(self.__get_dataset(table_index=table_index))
        self.assertTrue(form.is_valid())
        item_obj = form.save()
        self.assertEqual(item_obj, table_obj.objects.get())
            

    def test_form_validates_blank_items(self):
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table21, table_index="21")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table22, table_index="22")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table23, table_index="23")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table24, table_index="24")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table25, table_index="25")

        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table31, table_index="31")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table32, table_index="32")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table33, table_index="33")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table34, table_index="34")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table35, table_index="35")

        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table41, table_index="41")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table42, table_index="42")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table43, table_index="43")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table44, table_index="44")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table45, table_index="45")

        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table51, table_index="51")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table52, table_index="52")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table53, table_index="53")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table54, table_index="54")
        self.__test_form_dont_validates_blank_items_logic(form_obj=forms.Table55, table_index="55")



    def test_form_save(self):
        self.__test_form_save_logic(table_obj=models.Table21, form_obj=forms.Table21, table_index="21")
        self.__test_form_save_logic(table_obj=models.Table22, form_obj=forms.Table22, table_index="22")
        self.__test_form_save_logic(table_obj=models.Table23, form_obj=forms.Table23, table_index="23")
        self.__test_form_save_logic(table_obj=models.Table24, form_obj=forms.Table24, table_index="24")
        self.__test_form_save_logic(table_obj=models.Table25, form_obj=forms.Table25, table_index="25")

        self.__test_form_save_logic(table_obj=models.Table31, form_obj=forms.Table31, table_index="31")
        self.__test_form_save_logic(table_obj=models.Table32, form_obj=forms.Table32, table_index="32")
        self.__test_form_save_logic(table_obj=models.Table33, form_obj=forms.Table33, table_index="33")
        self.__test_form_save_logic(table_obj=models.Table34, form_obj=forms.Table34, table_index="34")
        self.__test_form_save_logic(table_obj=models.Table35, form_obj=forms.Table35, table_index="35")

        self.__test_form_save_logic(table_obj=models.Table41, form_obj=forms.Table41, table_index="41")
        self.__test_form_save_logic(table_obj=models.Table42, form_obj=forms.Table42, table_index="42")
        self.__test_form_save_logic(table_obj=models.Table43, form_obj=forms.Table43, table_index="43")
        self.__test_form_save_logic(table_obj=models.Table44, form_obj=forms.Table44, table_index="44")
        self.__test_form_save_logic(table_obj=models.Table45, form_obj=forms.Table45, table_index="45")

        self.__test_form_save_logic(table_obj=models.Table51, form_obj=forms.Table51, table_index="51")
        self.__test_form_save_logic(table_obj=models.Table52, form_obj=forms.Table52, table_index="52")
        self.__test_form_save_logic(table_obj=models.Table53, form_obj=forms.Table53, table_index="53")
        self.__test_form_save_logic(table_obj=models.Table54, form_obj=forms.Table54, table_index="54")
        self.__test_form_save_logic(table_obj=models.Table55, form_obj=forms.Table55, table_index="55")








    
   



         

   