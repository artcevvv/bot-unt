import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options = options)

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
    
    select= Select(driver.find_element(By.CSS_SELECTOR, '[formcontrolname = "testOrgOblId"]'))
    select.select_by_value('14')

    time.sleep(1)

    select2= Select(driver.find_element(By.CSS_SELECTOR, '[formcontrolname = "testOrgId"]'))
    select2.select_by_value('1052')

    select3= Select(driver.find_element(By.CSS_SELECTOR, '[formcontrolname = "testPeriodId"]'))
    # select3.select_by_visible_text('17.01.2024 14:30 (Свободных мест: 0)')
    options = select3.options

    global data
    data= []

    for item in options:
        variants= item.text
        data.append(variants)
        print(variants)
    
    return data

    


login()