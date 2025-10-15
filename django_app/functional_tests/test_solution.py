from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



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
                
                
                k_index = int(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-3").text) 
                
                row_n = int(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text) 
                table_index = int(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text + self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text)
                i = 0
                elements_arr_row1 = []
                element_arr_matrixB = []
                for i in range(1, row_n):
                    element_text = self.browser.find_element(By.ID, f"table{table_index}_row{i}_column1")
                    element_arr_matrixB.append(element_text)
                while i < row_n + 3:
                     i += 1
                     element_text = self.browser.find_element(By.ID, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-1-{i}").text
                     elements_arr_row1.append(element_text)
                
                
                r = 0
                i = 0
                k = 0
                while i < k_index+2:
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
                        obj_len = len(elements_arr_row1)
                        while e < obj_len:
                            e += 1
                            c += 1
                            
                            if e == 1:
                                self.assertEqual(int(self.browser.find_element(By.ID, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), k)
                            elif e == obj_len-1:
                                self.assertEqual(int(self.browser.find_element(By.ID, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), "-")
                            elif e == obj_len:
                                self.assertEqual(int(self.browser.find_element(By.ID, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), "")
                            else:
                                self.assertEqual(int(self.browser.find_element(By.ID, f"matrix-calculation-simple-iteration-method-block-block-step2-5-table-{r}-{c}").text), element_arr_matrixB[i])
                                i += 1
                    else:
                        pass


                    r += 1
                

    def __calculate_iteration(self, matrix_A: dict, matrix_B: dict, k: int=0) -> dict:
         """
         expecting the matrix elements in the format as matrix has tableXX, that has row1, row2, row3, .., rown
         """
         table = {}
         i = 0
         for k in matrix_A.keys():
            if not matrix_A.get(k):
                raise InvalidKeys(message="matrix_A is broken")
         if len(matrix_B) == 2:  
             table_row = {"x1", "x2"}
         elif len(matrix_B) == 3:
             table_row = {"x1", "x2", "x3"}
         elif len(matrix_B) == 4:
             table_row = {"x1", "x2", "x3", "x4"}
         elif len(matrix_B) == 5:
             table_row = {"x1", "x2", "x3", "x4", "x5"}
         while i < k: 
             table[str(i)] = table_row
             for k in table[str(i)].keys():
                 res = 0 
                 ### continue from here. it is the broken one
                 for k in matrix_A.keys():
                     elems_amount = len(matrix_A[k])
                     c = 0
                     for v in matrix_A[k].values():
                         for i in range(elems_amount):
                             if not table[str(i)].get(str(k)):
                                 c += 1
                                 res += v * table[str(i)][str(k)][f"x{c}"]
                             else:
                                 res += v * matrix_B[k][c]
                 table[str(i)][k] = res
            

