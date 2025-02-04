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
        driver.get("https://play.typeracer.com/")
        self.assertIn("TypeRacer", driver.title)
        time.sleep(2)
        but = (driver.find_element(By.ID, "gwt-uid-1")).find_element(By.CLASS_NAME, "prompt-button")
        but.click()

        time.sleep(2)
        t_find = (driver.find_element(By.CLASS_NAME, "timeDisplay")).find_element(By.CLASS_NAME, "time")
        while str(t_find.text) != "0:00":
            t_find = (driver.find_element(By.CLASS_NAME, "timeDisplay")).find_element(By.CLASS_NAME, "time")
            print(t_find.text)

        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()