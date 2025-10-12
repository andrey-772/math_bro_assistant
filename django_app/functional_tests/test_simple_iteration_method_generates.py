from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSimpleIterationSolution(FunctionalTest):
    def test_generates_if_data_is_valid(self):
        self.browser.get(self.live_server_url)
        
        for item_n in (2, 3, 4, 5):
            self.wait_for(lambda: self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1))
            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click()) 
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-anchor").text, "Solution")

           
            if item_n < 5:
                self.wait_for(lambda: self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)) 
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click()) 
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-anchor").text, "Solution")


    def test_not_generates_if_data_is_invalid(self):
        self.browser.get(self.live_server_url)
        
        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            print(f"{item_n}{item_n}")
            data_set = self.__get_dataset(table_index=f"{item_n}{item_n}")
            data_set2 = self.__get_dataset(table_index=f"{item_n}1")
            data_set.extend(data_set2)
            print(data_set, "data_set")
            for table_index in data_set:
                 field = self.browser.find_element(By.NAME, table_index)
                 field.send_keys(Keys.BACKSPACE)
                 self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                 self.wait_for(lambda: self.assertEqual(field.get_attribute("value"), ""))

                

            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                data_set = self.__get_dataset(table_index=f"{item_n+1}{item_n}")
                data_set2 = self.__get_dataset(table_index=f"{item_n+1}1")
                data_set.extend(data_set2)
                print(data_set)
                for table_index in data_set:
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                     self.wait_for(lambda: self.assertEqual(field.get_attribute("value"), ""))
        



    def test_generate_solution_without_losing_previous_data(self):
        self.browser.get(self.live_server_url)
        self.browser.get(self.live_server_url)
        
        for item_n in (2, 3, 4, 5):
            row1 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text
            column1 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text
            row2 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text
            column2 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text  
            self.wait_for(lambda: self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1))
            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click()) 
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-anchor").text, "Solution")
            self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text, row1)
            self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text, column1)
            self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text, row2)
            self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text, column2)


            if item_n < 5:
                row1 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text
                column1 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text
                row2 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text
                column2 = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text    
                self.wait_for(lambda: self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)) 
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click()) 
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-anchor").text, "Solution")
                self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text, row1)
                self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text, column1)
                self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3").text, row2)
                self.assertEqual(self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4").text, column2)


    def __get_dataset(self, table_index: str) -> list:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))
        return dataset_keys_list