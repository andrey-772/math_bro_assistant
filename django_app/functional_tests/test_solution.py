from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSolution(FunctionalTest):
    def test_given_solution_first_step_shows_correct_when_it_is_positive(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}")
            dataset2 = self.__get_dataset(table_index=f"{item_n}1")
            dataset.update(dataset2)
            for table_index in dataset.keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[table_index])
                     self.wait_for(lambda: self.assertEqual(float(field.get_attribute("value")), dataset[table_index]))
            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            print(dataset)
            a_index = self.__calculate_A_index(dataset)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-main-text").text, "Solution")
            self.assertIn(str(a_index), self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
            self.assertIn(">", self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
 
            if item_n < 5:
                self.generate_matrix(elem_n=item_n-1, elem_n2=item_n)
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}")
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1")
                dataset.update(dataset2)
                for table_index in dataset.keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[table_index])
                         self.wait_for(lambda: self.assertEqual(float(field.get_attribute("value")), dataset[table_index]))
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                print(dataset)
                a_index = self.__calculate_A_index(dataset)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-main-text").text, "Solution")
                self.assertIn(str(a_index), self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
                self.assertIn(">", self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)


    def test_given_solution_first_step_shows_correct_when_it_is_negative(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.__get_dataset(table_index=f"{item_n}{item_n}", negative=True)
            dataset2 = self.__get_dataset(table_index=f"{item_n}1", negative=True)
            dataset.update(dataset2)
            for table_index in dataset.keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[table_index])
                     self.wait_for(lambda: self.assertEqual(float(field.get_attribute("value")), dataset[table_index]))
            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            print(dataset)
            a_index = self.__calculate_A_index(dataset)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-main-text").text, "Solution")
            self.assertIn(str(a_index), self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
            self.assertIn("<", self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
 
            if item_n < 5:
                self.generate_matrix(elem_n=item_n-1, elem_n2=item_n)
                dataset = self.__get_dataset(table_index=f"{item_n+1}{item_n}", negative=True)
                dataset2 = self.__get_dataset(table_index=f"{item_n+1}1", negative=True)
                dataset.update(dataset2)
                for table_index in dataset.keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[table_index])
                         self.wait_for(lambda: self.assertEqual(float(field.get_attribute("value")), dataset[table_index]))
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                print(dataset)
                a_index = self.__calculate_A_index(dataset)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-main-text").text, "Solution")
                self.assertIn(str(a_index), self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)
                self.assertIn("<", self.browser.find_element(By.CLASS_NAME, "matrix-calculation-simple-iteration-method-block-block-step1-A").text)


       


    def __calculate_A_index(self, tables_data):
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
        return max(row_values)
       

    def __get_dataset(self, table_index: str, negative: bool=False) -> list:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))
        
        data = {}   
        value = 1
        if negative:
            value = -1 
        for k in dataset_keys_list:
            data[k] = value
            value += 1
            if negative:
                value -= 2
        return data