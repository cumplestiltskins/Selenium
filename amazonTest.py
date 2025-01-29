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

genai.configure(api_key="AIzaSyBi-lF7PEra0qfk-1CKxaLnoEEZGqICY1k")

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def captcha(self, src, driver):
        print("captcha executed")
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        image = httpx.get(src)
        prompt = "what is the text in this image"
        response = model.generate_content([{'mime_type':'image/jpeg', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])
        cap = response.text
        print(cap)
        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "field-keywords")))
        elem.send_keys(f"{cap}")
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        

    def test_search_in_python_org(self):
        
        driver = self.driver
        driver.get("http://www.amazon.in")
        self.assertIn("Amazon", driver.title)

        try:
            elem = driver.find_element(By.NAME, "field-keywords")
            elem.send_keys("earphone", Keys.SHIFT, "wireless ")
            elem.send_keys(Keys.RETURN)
        except Exception as e:
            print(e)
            

        while j!=5:
            current_url = driver.current_url
            if "validateCaptcha" in current_url:
                break
            time.sleep(1)  
            j+=1

        print(current_url)

        if "validateCaptcha" in current_url:
            print("executed")
            srcEl = driver.find_element(By.TAG_NAME, "IMG")
            src = srcEl.get_attribute("src")
            print(src)
            self.captcha(src, driver)
            
        i=2
        while i != 10:
            time.sleep(5)
            print(i)
            element = driver.find_element(By.XPATH, f'//*[@aria-label="Go to page {i}"]')
            i+=1
            elmn = driver.find_element(By.CLASS_NAME, "a-price-whole")
            txt = ","
            txt1 = elmn.text
            if txt in txt1:
                txt1= txt1.replace(txt,"")
            if int(txt1) < 1500:
                print(elmn.text, "is cheap!")
            element.click()
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    