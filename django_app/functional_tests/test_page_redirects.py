from .base import FunctionalTest
from selenium.webdriver.common.by import By


class TestRedirectsWorks(FunctionalTest):
    def test_redirects_when_click_on_logo(self):
        self.browser.get(self.live_server_url)
        logo = self.browser.find_element(By.ID, "top-frame-logo")
        self.wait_for(lambda: self.assertEqual(logo.text, "Math Assistant"))
        logo.click()
        logo = self.browser.find_element(By.ID, "top-frame-logo")
        self.wait_for(lambda: self.assertEqual(logo.text, "Math Assistant"))
        logo.click()
        
        