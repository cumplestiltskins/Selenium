import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Edge()

	def functionality(self, words):
		wordList = []

		for i in words:
			wordList.append(i.text)
		result = ''.join(wordList)
		return result
	
	def checkComma(self, span):
		for i in span:
			if ',' in i.text:
				return ','
		return ''

		

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("https://play.typeracer.com/")
		self.assertIn("TypeRacer", driver.title)
		time.sleep(2)
		but = (driver.find_element(By.ID, "gwt-uid-1")).find_element(By.CLASS_NAME, "prompt-button")
		but.click()

		time.sleep(2)

		span = driver.find_elements(By.TAG_NAME, "span")
		for i in span:
			if len(i.text) >100 :
				words = i.text 
		#main_div = input("enter main div: ")
		#
		#div = driver.find_element(By.CLASS_NAME, main_div)y - no
		
		wp = driver.find_element(By.CLASS_NAME, "txtInput")
		ss = input()
		time.sleep(2)
		

		for i in words:
			wp.send_keys(i)


		self.assertNotIn("No results found.", driver.page_source)


	def tearDown(self):
		time.sleep(100)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
