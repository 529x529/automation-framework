import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    print("Start Test 1")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_customer_information()

    pg = Payment_page(driver)
    pg.payment()

    f = Finish_page(driver)
    f.finish()


    print("Finish test 1")
    # time.sleep(5)
    driver.quit()

# @pytest.mark.run(order=1)
# def test_buy_product_2(set_up, set_group):
#     driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')
#
#     print("Start Test 2")
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_2()
#
#     cp = Cart_page(driver)
#     cp.product_confirmation()
#
#
#     print("Finish test 2")
#     # time.sleep(5)
#     driver.quit()
#
# # @pytest.mark.run(order=2)
# def test_buy_product_3(set_up, set_group):
#     driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')
#
#     print("Start Test 3")
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_3()
#
#     cp = Cart_page(driver)
#     cp.product_confirmation()
#
#
#     print("Finish test 3")
#     # time.sleep(5)
#     driver.quit()