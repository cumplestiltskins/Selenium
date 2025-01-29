import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/1333104896278396939")
        time.sleep(5)
        self.assertIn("Discord", driver.title)
        elem = driver.find_element(By.CLASS_NAME, "container_b2ca13")
        mask = elem.find_element(By.TAG_NAME, "mask")
        print(mask.get_attribute)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()