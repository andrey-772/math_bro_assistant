from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class TestSolution(FunctionalTest):
    def test_given_solution_first_step_shows_correct_when_A_is_bigger_than_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}")
            dataset2 = self.__get_dataset(table_index=f"{item_n}1")
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])
            

            for table_index in dataset[1].keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            data = self.__calculate_convergence(dataset[0])
            a, b = data[0], data[1]
            self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(">", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)


            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}")
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1")
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1]) 
                for table_index in dataset[1].keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                data = self.__calculate_convergence(dataset[0])
                a, b = data[0], data[1]
                #time.sleep(10)
                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(">", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)


    def test_given_solution_first_step_shows_correct_when_A_is_equals_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", is_1=True)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", is_1=True)
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])

            for table_index in dataset[1].keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            print(dataset[0], dataset[1])
            data = self.__calculate_convergence(dataset[0])
            a, b = data[0], data[1]
            self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn("=", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)


            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", is_1=True)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", is_1=True)
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1])

                for table_index in dataset[1].keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
    
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                print(dataset[0], dataset[1])
                data = self.__calculate_convergence(dataset[0])
                a, b = data[0], data[1]
                time.sleep(5)
                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn("=", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)



    def test_given_solution_first_step_shows_correct_when_A_is_lower_than_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", small=True)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", small=True)
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])
            for table_index in dataset[1].keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            print(dataset[0], dataset[1])
            data = self.__calculate_convergence(dataset[0])
            a, b = data[0], data[1]
            self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)


            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", small=True)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", small=True)
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1])
                for table_index in dataset[1].keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
    
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                print(dataset[0], dataset[1])
                data = self.__calculate_convergence(dataset[0])
                a, b = data[0], data[1]
                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)


       


    def __calculate_convergence(self, tables_data: dict) -> list:
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


    def __get_dataset(self, table_index: str, small: bool=False, is_1: bool=False) -> list:
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
            data[k] = value
            data_2[k] = value2

        return [data, data_2]

