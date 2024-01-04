from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get('https://app.testcenter.kz/auth')


def login():
    login= ''
    password= ''
    driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(login)
    driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)

    driver.find_element(By.TAG_NAME, 'button').click()

    WebDriverWait(driver, 20)

login()