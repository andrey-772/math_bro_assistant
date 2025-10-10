from .base import FunctionalTest
from selenium.webdriver.common.by import By
import time

class TestSimpleIterationSolution(FunctionalTest):
    def test_generates_if_data_is_valid(self):
        self.browser.get(self.live_server_url)
        
        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            print(f"{item_n}{item_n}")
            data_set = self.__get_dataset(table_index=f"{item_n}{item_n}")
            for table_index in data_set:
                 self.assertEqual(self.browser.find_element(By.NAME, table_index).get_attribute("value"), "0")

           
            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1) 
                data_set = self.__get_dataset(table_index=f"{item_n+1}{item_n}")
                print(data_set)
                for table_index in data_set:
                     self.assertEqual(self.browser.find_element(By.NAME, table_index).get_attribute("value"), "0")


    def __get_dataset(self, table_index: str) -> list:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))
        return dataset_keys_list