import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import google.generativeai as genai
import httpx
import os
import base64
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):

	def captcha(self, src, driver):
		print("captcha executed")
		model = genai.GenerativeModel(model_name="gemini-1.5-pro")
		image = httpx.get(src)
		prompt = "what is the text in this image. be very accurate about the answer and make the answer in a single line"
		response = model.generate_content([{'mime_type':'image/jpeg', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])
		cap = response.text
		print(cap)	

		textf = driver.find_element(By.CLASS_NAME, "challengeTextArea")
		for i in cap:
			textf.send_keys(i)
		

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

		
		wp = driver.find_element(By.CLASS_NAME, "txtInput")
		ss = input()
		time.sleep(2)
		

		for i in words:
			wp.send_keys(i)

		time.sleep(1)
		but = driver.find_element(By.CLASS_NAME, "gwt-Button")
		but.click()

		time.sleep(1)
		src = driver.find_element(By.CLASS_NAME, "challengeImg").get_attribute("src")
		print(src)
		self.captcha(src, driver)

		self.assertNotIn("No results found.", driver.page_source)


	def tearDown(self):
		time.sleep(100)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

#challengeImg challengeTextArea