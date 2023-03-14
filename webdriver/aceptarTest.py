import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# create webdriver object

browser = webdriver.Chrome()
browser.implicitly_wait(0.5)
browser.maximize_window()


# URL of the website
url = "https://www.e-pacallianz.com/idp/"
browser.get(url)

# Getting current URL source code
#identify element
inputUser = browser.find_element(By.ID,"j_username")
inputUser.send_keys("e107580")


inputPw = browser.find_element(By.ID,"j_password")
inputPw.send_keys("JaimePuto33")

time.sleep(15)
btnAceptar = browser.find_element(By.ID,"btn_center")
btnAceptar.click()

time.sleep(25)
browser.quit()