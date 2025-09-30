from django.db.models import Q
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time


class TestGenerateMatrix(FunctionalTest):
	def test_generate_matrix_elements_in_place(self):
		self.browser.get(self.live_server_url)
		element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1")
		self.assertEqual(element.text, "3")

		element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2")
		self.assertEqual(element.text, "3")

		element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-3")
		self.assertEqual(element.text, "3")

		element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-4")
		self.assertEqual(element.text, "1")


	def test_generate_matrix_js_works_properly(self):
		self.browser.get(self.live_server_url)
		for elem_n in (1, 2, 3, 4):
			element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-1")
			element.click()
			self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-1-option-{elem_n}").click()
			self.assertEqual(element.text, f"{elem_n+1}")


		for elem_n in (1, 2, 3, 4):
			element = self.browser.find_element(By.ID, "generate-the-matrix-block-table-section-button-2")
			element.click()
			self.browser.find_element(By.ID, f"generate-the-matrix-block-table-section-button-2-option-{elem_n}").click()
			self.assertEqual(element.text, f"{elem_n+1}")

			

	