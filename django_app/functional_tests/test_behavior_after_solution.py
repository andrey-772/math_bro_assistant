from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAfterSolution(FunctionalTest):
    def test_inner_elements_shown_properly(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.get_dataset(table_index=f"{item_n}{item_n}", small=True)
            dataset2 = self.get_dataset(table_index=f"{item_n}1", small=True)
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])
            for table_index in dataset[1].keys():
                     field = self.wait_for(lambda: self.browser.find_element(By.NAME, table_index))
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())

            self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
            element_text = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text
            inner_element=self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{int(element_text)-1}")
            self.assertIn("active", inner_element.get_attribute("class"))


            element_text = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text
            inner_element=self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{int(element_text)-1}")
            self.assertIn("active", inner_element.get_attribute("class"))


            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.get_dataset(table_index=f"{item_n+1}{item_n}", small=True)
                dataset2 = self.get_dataset(table_index=f"{item_n+1}1", small=True)
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1])
                for table_index in dataset[1].keys():
                         field = self.wait_for(lambda: self.browser.find_element(By.NAME, table_index))
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
                
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())


                self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
                element_text = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1").text
                inner_element=self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{int(element_text)-1}")
                self.assertIn("active", inner_element.get_attribute("class"))


                element_text = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2").text
                inner_element=self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{int(element_text)-1}")
                self.assertIn("active", inner_element.get_attribute("class"))




       