import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


def test_select_product(self):
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    print("Start Test")

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id = 'shopping_cart_container']")))
    enter_shopping_cart.click()
    print("Click enter shopping cart")