from .base import FunctionalTest
from selenium.webdriver.common.by import By


class TestSolution(FunctionalTest):
    def test_given_solution_shows_correct(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-main-text").text, "Solution")

        dataset = self.__get_dataset(table_index="33")
        dataset2 = self.__get_dataset(table_index="31")
        dataset.update(dataset2)
        


    def calculate_A_index(tables_data):
        table_indexes = []
        form_data = {}
        rows_table_1 = []
        rows_table_2 = []
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
                    form_data[str(table_indexes[0])].get(k[8:11]) = []
                form_data[str(table_indexes[0])][8:11].append(v)
            elif c == 2:
                if k[8:11] not in rows_table_2:
                    rows_table_2.append(k[8:11])
                if form_data.get(str(table_indexes[1])) is None:
                    form_data[str(table_indexes[1])] = {}
                if form_data[str(table_indexes[1])].get(k[8:11]) is None:
                    form_data[str(table_indexes[1])].get(k[8:11]) = []
                form_data[str(table_indexes[1])][8:11].append(v)


        row_values = []
        for row in rows_table_1:
            row_abs = []
            for i in form_data[table_indexes[0]][row]:
                row_abs.append(abs(i))
            row_values.append(max(row_abs))
        return max(row_values)
       

    def __get_dataset(self, table_index: str) -> list:
        dataset_keys_list = []
        for row_index in range(1, int(table_index[0])+1):
              for column_index in range(1, int(table_index[1])+1):
                   dataset_keys_list.append("table"+table_index+"_row"+str(row_index)+"_column"+str(column_index))
        
        data = {}   
        value = 1
        for k in dataset_keys_list:
            data[k] = value
            value += 1
        return data