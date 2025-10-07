from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestMatrixTableGenerated(FunctionalTest):
    def test_matrix_table_elements_in_place(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()

        matrix_block1_name = self.browser.find_element(By.ID, "matrix-table-block-block1-name").text
        matrix_block2_name = self.browser.find_element(By.ID, "matrix-table-block-block2-name").text
       
        self.assertEqual(matrix_block1_name, "Matrix A")
        self.assertEqual(matrix_block2_name, "Matrix B")

        for i in (2, 3, 4, 5):
            amount_of_rows1 = i
            amount_of_rows2 = i
            elem_n = i -1


            self.__generate_matrix(elem_n)

            self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()

            if amount_of_rows1 == 2:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table22-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table33-row1-column1")), 0)
            elif amount_of_rows1 == 3:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table33-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table44-row1-column1")), 0)
            elif amount_of_rows1 == 4:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table44-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table55-row1-column1")), 0)
            elif amount_of_rows1 == 5:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table55-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table22-row1-column1")), 0)


            if amount_of_rows2 == 2:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table21-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table31-row1-column1")), 0)
            elif amount_of_rows2 == 3:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table31-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table41-row1-column1")), 0)
            elif amount_of_rows2 == 4:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table41-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table51-row1-column1")), 0)
            elif amount_of_rows2 == 5:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table51-row1-column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table21-row1-column1")), 0)




    def test_matrix_can_be_filled(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()


        for i in (2, 3, 4, 5):
            amount_of_rows1 = i
            amount_of_rows2 = i
            elem_n = i -1

            self.DATA_SET = (["-1", "--1"], ["123", "--1"], ["1,9", "+1"], ["123,01", "1,,0"])

            self.__generate_matrix(elem_n)

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click())
            
            if amount_of_rows1 == 2:
                 self.__test_matrix_can_be_filled_check_variants(table_id="table21", rows=2, columns=1)
                 self.__test_matrix_can_be_filled_check_variants(table_id="table22", rows=2, columns=2)
            elif amount_of_rows1 == 3:
                 self.__test_matrix_can_be_filled_check_variants(table_id="table33", rows=3, columns=3)
            elif amount_of_rows1 == 4:
                 self.__test_matrix_can_be_filled_check_variants(table_id="table44", rows=4, columns=4)
            elif amount_of_rows1 == 5:
                 self.__test_matrix_can_be_filled_check_variants(table_id="table55", rows=5, columns=5)


            if amount_of_rows2 == 2:
                self.__test_matrix_can_be_filled_check_variants(table_id="table21", rows=2, columns=1)
            elif amount_of_rows2 == 3:
                self.__test_matrix_can_be_filled_check_variants(table_id="table31", rows=3, columns=1)
            elif amount_of_rows2 == 4:
                self.__test_matrix_can_be_filled_check_variants(table_id="table41", rows=4, columns=1)
            elif amount_of_rows2 == 5:
                self.__test_matrix_can_be_filled_check_variants(table_id="table51", rows=5, columns=1)    


    def __iter_and_test_through_data_set(self, elem_id):
        for i in self.DATA_SET:
                    input_form = self.browser.find_element(By.NAME, elem_id)
                    input_form.clear()
                    input_form.send_keys(i[0])
                    self.assertEqual(input_form.get_attribute("value"), i[0])

                    input_form.clear()
                    input_form.send_keys(i[1])
                    self.assertNotEqual(input_form.get_attribute("value"), i[1]) 


    def __generate_matrix(self, elem_n):
            self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1")
            element.click()
            
            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{elem_n}").click()
            self.assertEqual(element.text, f"{elem_n+1}")
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2")
            element.click()

            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{elem_n}").click()
            self.assertEqual(element.text, f"{elem_n+1}")



    def __test_matrix_can_be_filled_check_variants(self, table_id, rows, columns):
                  for row in range(1, rows+1):          
                        for column in range(1, columns+1):   
                            elem_id = f"{table_id}-row{row}-column{column}"
                            self.wait_for(lambda: self.__iter_and_test_through_data_set(elem_id=elem_id))