import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
import pytest


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get('https://app.testcenter.kz/auth')


def login():
    login= ''
    password= ''
    driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(login)
    driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)

    driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"text-3xl").click()
    time.sleep(2)

    divs = driver.find_elements(By.CLASS_NAME, 'text-2xl')
    divs[1].click()           
    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"p-3").click()
    time.sleep(2)

    btns= driver.find_elements(By.CLASS_NAME, "p-3")
    btns[0].click()
    time.sleep(2)

    collapse= driver.find_elements(By.CLASS_NAME, 'mb-4')
    collapse[0].click()

    collapse[3].click()

    selects= driver.find_elements(By.TAG_NAME, 'select')
    
    select= Select(selects[0])
    with pytest.raises(NotImplementedError):
        select.select_by_value('14')
    time.sleep(3)
    


login()