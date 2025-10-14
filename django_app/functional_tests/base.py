from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import math


MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        if test_server := os.environ.get("TEST_SERVER"):
            self.live_server_url = "http://" + test_server
			

    def tearDown(self):
        self.browser.quit()


    def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    print("!!!")
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn


    @wait
    def wait_for(self, fn):
        return fn()

    
    @wait
    def generate_matrix(self, elem_n=1, elem_n2=1):
            self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1")
            element.click()
            
            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{elem_n}").click()
            self.assertEqual(element.text, f"{elem_n+1}")
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2")
            element.click()

            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{elem_n2}").click()
            self.assertEqual(element.text, f"{elem_n2+1}")

            self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()


    def calculate_convergence(self, tables_data: dict) -> list:
        table_indexes = []
        form_data = {}
        rows_table_1 = []
        rows_table_2 = []
        c = 0
        for k, v in tables_data.items():
            if k[5:7] not in table_indexes:
                c += 1
                table_indexes.append(k[5:7])
            if c == 1:
                if k[8:11] not in rows_table_1:
                    rows_table_1.append(k[8:11])
                if form_data.get(str(table_indexes[0])) is None:
                    form_data[str(table_indexes[0])] = {}
                if form_data[str(table_indexes[0])].get(k[8:11]) is None:
                    form_data[str(table_indexes[0])][k[8:11]] = []
                form_data[str(table_indexes[0])][k[8:11]].append(v)
            elif c == 2:
                if k[8:11] not in rows_table_2:
                    rows_table_2.append(k[8:11])
                if form_data.get(str(table_indexes[1])) is None:
                    form_data[str(table_indexes[1])] = {}
                if form_data[str(table_indexes[1])].get(k[8:11]) is None:
                    form_data[str(table_indexes[1])][k[8:11]] = []
                form_data[str(table_indexes[1])][k[8:11]].append(v)


        row_values = []
        for row in rows_table_1:
            row_abs = []
            for i in form_data[table_indexes[0]][row]:
                row_abs.append(abs(i))
            row_values.append(max(row_abs))


        row_values2 = []
        for row in rows_table_2:
            row_abs = []
            for i in form_data[table_indexes[1]][row]:
                row_abs.append(abs(i))
            row_values2.append(max(row_abs))

        return [max(row_values), max(row_values2)]


    def get_dataset(self, table_index: str, small: bool=False, is_1: bool=False, is_0: bool=False) -> list:
        """
        the first element is the list for an internal manipulations, 
        the second element is the list for the external view
        """
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))
        

        data = {}   
        data_2 = {}
        for k in dataset_keys_list:
            value = random.randint(-1000000, 1000000)
            value2 = value
            if small:
                value =  round(random.uniform(0.1, 0.9), 3)
                proper_value = ""
                for i in str(value):
                    if i == ".":
                        proper_value += ","
                    else:
                        proper_value += i
                value2 = proper_value
            if is_1:
                value = 1
                value2 = 1
            if is_0:
                value = 0
                value2 = 0
            data[k] = value
            data_2[k] = value2

        return [data, data_2]


    
    def calculate_k(self, a:float, b:float) -> float:
        equation = (math.log10(0.001) + math.log10(1-a) - math.log10(b))/math.log10(a)
        return equation
