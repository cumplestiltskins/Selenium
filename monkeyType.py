import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def functionality(self, letter):
        wordList = []

        for i in letter:
            wordList.append(i.text)
        
        result = ''.join(wordList)
        return result
        

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://monkeytype.com/")
        self.assertIn("Monkeytype", driver.title)
        time.sleep(2)
        clck = driver.find_element(By.CLASS_NAME, "acceptAll")
        clck.click()
        time.sleep(2)
        
        elem = driver.find_element(By.ID, "words")

        i=0
        while i!=100:
            active = elem.find_element(By.CLASS_NAME, "active")
            letter = active.find_elements(By.TAG_NAME, "letter")
            word = self.functionality(letter)
            pyautogui.write(f"{word} " , interval=0.025)
            i += 1

        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()