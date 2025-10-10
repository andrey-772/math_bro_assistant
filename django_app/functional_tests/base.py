from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        if test_server := os.environ.get("TEST_SERVER"):
            self.live_server_url = "http://" + test_server
			

    def tearDown(self):
        self.browser.quit()


    def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    print("!!!")
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn


    @wait
    def wait_for(self, fn):
        return fn()

    
    @wait
    def generate_matrix(self, elem_n=1, elem_n2=1):
            self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1")
            element.click()
            
            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{elem_n}").click()
            self.assertEqual(element.text, f"{elem_n+1}")
            element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2")
            element.click()

            self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{elem_n2}").click()
            self.assertEqual(element.text, f"{elem_n2+1}")

            self.browser.find_element(By.CLASS_NAME, "generate-the-matrix-block-button-generate").click()
