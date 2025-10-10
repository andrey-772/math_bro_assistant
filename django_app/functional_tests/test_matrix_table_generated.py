from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


            self.generate_matrix(elem_n=elem_n, elem_n2=elem_n)

            if amount_of_rows1 == 2:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table22_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table33_row1_column1")), 0)
            elif amount_of_rows1 == 3:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table33_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table44_row1_column1")), 0)
            elif amount_of_rows1 == 4:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table44_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table55_row1_column1")), 0)
            elif amount_of_rows1 == 5:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table55_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table22_row1_column1")), 0)


            if amount_of_rows2 == 2:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table21_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table31_row1_column1")), 0)
            elif amount_of_rows2 == 3:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table31_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table41_row1_column1")), 0)
            elif amount_of_rows2 == 4:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table41_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table51_row1_column1")), 0)
            elif amount_of_rows2 == 5:
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table51_row1_column1")), 1)
                self.assertEqual(len(self.browser.find_elements(By.NAME, "table21_row1_column1")), 0)




    def test_matrix_can_be_filled(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()


        for i in (2, 3, 4, 5):
            amount_of_rows1 = i
            amount_of_rows2 = i
            elem_n = i -1

            self.DATA_SET = (["-1", "--1"], ["123", "--1"], ["1,9", "+1"], ["123,01", "1,,0"])

            self.generate_matrix(elem_n=elem_n, elem_n2=elem_n)
            
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

           
    def __test_matrix_can_be_filled_check_variants(self, table_id, rows, columns):
                  for row in range(1, rows+1):          
                        for column in range(1, columns+1):   
                            elem_id = f"{table_id}_row{row}_column{column}"
                            self.wait_for(lambda: self.__iter_and_test_through_data_set(elem_id=elem_id))