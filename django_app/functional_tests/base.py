from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
import os
from selenium.webdriver.common.action_chains import ActionChains


MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.actions = ActionChains(self.browser)
		if test_server := os.environ.get("TEST_SERVER"):
			self.live_server_url = "http://" + test_server
			


	def tearDown(self):
		self.browser.quit()