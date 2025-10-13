from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math


class TestSolution(FunctionalTest):
    def test_given_solution_first_step_shows_correct_when_A_is_bigger_than_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.get_dataset(table_index=f"{item_n}{item_n}")
            dataset2 = self.get_dataset(table_index=f"{item_n}1")
            dataset[0].update(dataset2[0])
            dataset[1].update(dataset2[1])
            

            for table_index in dataset[1].keys():
                     field = self.browser.find_element(By.NAME, table_index)
                     field.send_keys(Keys.BACKSPACE)
                     field.send_keys(dataset[1][table_index])

            self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
            data = self.calculate_convergence(dataset[0])
            a, b = data[0], data[1]
            time.sleep(3)
            self.wait_for(lambda: self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text))
            self.assertIn(">", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is not convergent")
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "")


            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.get_dataset(table_index=f"{item_n+1}{item_n}")
                dataset2 = self.get_dataset(table_index=f"{item_n+1}1")
                dataset[0].update(dataset2[0])
                dataset[1].update(dataset2[1]) 
                for table_index in dataset[1].keys():
                         field = self.browser.find_element(By.NAME, table_index)
                         field.send_keys(Keys.BACKSPACE)
                         field.send_keys(dataset[1][table_index])
                self.wait_for(lambda: self.browser.find_element(By.CLASS_NAME, "matrix-table-block-submit-button").click())
                data = self.calculate_convergence(dataset[0])
                a, b = data[0], data[1]
                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(">", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is not convergent")
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "")


    def test_given_solution_first_step_shows_correct_when_A_is_equals_1(self):
        self.browser.get(self.live_server_url)

        for item_n in (2, 3, 4, 5):
            self.generate_matrix(elem_n=item_n-1, elem_n2=item_n-1)
            dataset = self.get_dataset(table_index=f"{item_n}{item_n}", is_1=True)
            dataset2 = self.get_dataset(table_index=f"{item_n}1", is_1=True)
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
            time.sleep(3)
            self.wait_for(lambda: self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text))
            self.assertIn("=", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is not convergent")
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "")

            if item_n < 5:
                self.generate_matrix(elem_n=item_n, elem_n2=item_n-1)
                dataset = self.get_dataset(table_index=f"{item_n+1}{item_n}", is_1=True)
                dataset2 = self.get_dataset(table_index=f"{item_n+1}1", is_1=True)
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
                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn("=", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is not convergent")
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "")



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
            time.sleep(3)
            self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
            self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is convergent")
            self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "2. Calculating the iteration number")


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
                k = self.__calculate_k(a=a, b=b)
                print(str(round(k, 3)), int(k))


                self.assertIn(str(a), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn("<", self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-2").text)
                self.assertIn(str(b), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-3").text)
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step1-4").text, "System is convergent")
                self.assertEqual(self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-1-text").text, "2. Calculating the iteration number")

                self.assertIn(str(round(k, 3)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-2").text)
                self.assertIn(str(int(k)), self.browser.find_element(By.ID, "matrix-calculation-simple-iteration-method-block-block-step2-3").text)


    def __calculate_k(self, a:float, b:float):
        equation = (math.log10(0.001) + math.log10(1-a) - math.log10(b))/math.log10(a)
        return equation
