import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product():
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    print("Start Test")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_customer_information()

    time.sleep(5)
