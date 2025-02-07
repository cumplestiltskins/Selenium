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

        main_div = input("enter main div: ")
        
        div = driver.find_element(By.CLASS_NAME, main_div)
        

        word_class = input("enter word class: ")

        time.sleep(5)
        words = driver.find_elements(By.CLASS_NAME, word_class)
        
        for i in range(100):
            
            span = div.find_elements(By.TAG_NAME, "span")
            words = driver.find_elements(By.CLASS_NAME, word_class)
            pyautogui.write(f"{self.functionality(words)}{self.checkComma(span)} ", interval=0)


        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()