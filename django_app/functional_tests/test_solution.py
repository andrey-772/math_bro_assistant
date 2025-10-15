from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class InvalidKeys(Exception):
        """Exception raised for InvalidKeys scenarios.

        Attributes:
            message -- explanation of the error
        """

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)



class TestSolution(FunctionalTest):
    def test_given_solution_first_step_and_next_steps_shows_correct_when_A_is_lower_than_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.get_dataset(table_index=f"{item_n}{item_n}", small=True)
            dataset2 = self.get_dataset(table_index=f"{item_n}1", small=True)
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])
            for table_index in dataset[1].keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            print(dataset[0], dataset[1])
            data = self.calculate_convergence(dataset[0])
            a, b = data[0], data[1]
            k = self.calculate_k(a=a, b=b)
            
            self.wait_for(lambda: self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text))
            self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is convergent")
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "2. Calculating the iteration number")

            self.assertIn(str(round(k, 3)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-2").text)
            self.assertIn(str(int(k)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-3").text)



            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.get_dataset(table_index=f"{item_n+1}{item_n}", small=True)
                dataset2 = self.get_dataset(table_index=f"{item_n+1}1", small=True)
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1])
                for table_index in dataset[1].keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
                
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                data = self.calculate_convergence(dataset[0])
                a, b = data[0], data[1]
                k = self.calculate_k(a=a, b=b)
                print(str(round(k, 3)), int(k))

                self.wait_for(lambda: self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text))

                self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is convergent")
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "2. Calculating the iteration number")

                self.assertIn(str(round(k, 3)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-2").text)
                self.assertIn(str(int(k)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-3").text)
                
                self.__second_part_given_solution_first_step_and_next_steps_shows_correct_when_A_is_lower_than_1(dataset, k_index=int(k))


    def __second_part_given_solution_first_step_and_next_steps_shows_correct_when_A_is_lower_than_1(self, dataset, k_index):                
                row_n = int(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text) 
                table_index = int(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text + self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text)
                
                elements_arr_row1 = []
                element_arr_matrixB = []
                self.browser.execute_script("window.scrollBy(0, -300);")
                for i in range(1, row_n):
                    element_text = self.browser.find_element(By.NAME, f"table{table_index}_row{i}_column1")
                    element_arr_matrixB.append(element_text)
                self.browser.execute_script("window.scrollBy(0, 300);")
                i = 0
                while i < row_n+3:
                     i += 1
                     element_text = self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-1-{i}").text
                     elements_arr_row1.append(element_text)
                r = 0
                i = 0
                k = 0
                obj_len = row_n + 3
                matrixA, matrixB =  self.__collect_data_from_matrix_tables(dataset[0])
                data = self.__calculate_iteration(matrix_A=matrixA, matrix_B=matrixB, k=k_index)
                while r < k_index+2:
                    if r == 1:
                        self.assertEqual(elements_arr_row1[0], "k")
                        self.assertEqual(elements_arr_row1[-1], "")
                        self.assertEqual(elements_arr_row1[-2], "Δ")
                        c = 0
                        i = 0
                        for element in elements_arr_row1:
                            if element not in ("k", "", "Δ"):
                                i += 1
                                self.assertEqual(elements_arr_row1[c], f"x{i}")
                            c += 1
                    elif r == 2:
                        e = 0
                        c = 0
                        i = 0
                        while e < obj_len:
                            e += 1
                            c += 1
                            
                            if e == 1:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), k)
                            elif e == obj_len-1:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), "-")
                            elif e == obj_len:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), "")
                            else:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), element_arr_matrixB[i])
                                i += 1
                    else:
                        e = 0
                        c = 0
                        i = 1
                        while e < obj_len:
                            e += 1
                            c += 1
                            if e == 1:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), k)
                            elif e == obj_len:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), "")
                            else:
                                self.assertEqual(int(self.browser.find_element(By.NAME, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), data[str(r-2)][f"x{i}"]) 
                                i += 1
                    r += 1
                

    def __collect_data_from_matrix_tables(self, tables_data: dict) -> list:
        """
        returns the array, where the first element is the dict of elements from matrix A,
        the second element is the dict of elements from matrix B.
        """
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
        return [form_data[str(table_indexes[0])], form_data[str(table_indexes[1])]]


    def __calculate_iteration(self, matrix_A: dict, matrix_B: dict, k: int=0) -> dict:
         """
         expects the matrix elements in the format as matrix has tableXX, that has row1, row2, row3, .., rown
         """
         table = {}
         i = 0
         x_amount = len(matrix_B)
         for k in matrix_A.keys():
            if not matrix_A.get(k):
                raise InvalidKeys(message="matrix_A is broken")
         if x_amount == 2:  
             table_row = {"x1", "x2"}
         elif x_amount == 3:
             table_row = {"x1", "x2", "x3"}
         elif x_amount == 4:
             table_row = {"x1", "x2", "x3", "x4"}
         elif x_amount == 5:
             table_row = {"x1", "x2", "x3", "x4", "x5"}
         while i < k: 
             table[str(i)] = table_row
             for r in table[str(i)].keys():
                 res = 0 
                 for k in matrix_A.keys():
                     if i == 0:
                         table[str(i)][r] = matrix_B[k]
                         continue
                     for v in matrix_A[k].values():
                          if not table[str(i)].get(r):
                              res += v * table[str(i)][r]
                          else:
                              res += v * matrix_B[k][0]
                 table[str(i)][r] = res
             i += 1
         elements_in_row = []
         elements_in_row2 = []
         for table_row in table.values():
             for value in table_row.values():
                 if len(elements_in_row) == x_amount:
                     elements_in_row2.append(value)
                 else:
                     elements_in_row.append(value)
             table_row["delta"] = abs(max(elements_in_row2)-max(elements_in_row)) 
             elements_in_row = elements_in_row2
             elements_in_row2 = []
         return table
           
