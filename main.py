from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

URL = "https://orteil.dashnet.org/cookieclicker/"

driver.get(URL)
driver.implicitly_wait(10)
cookie = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
cookie.click()

while True:
    cookie_button = driver.find_element(By.ID, value="bigCookie")
    driver.implicitly_wait(30)
    cookie_button.click()