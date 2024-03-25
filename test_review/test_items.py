import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_bascket(browser):
    browser.get(link)
    time.sleep(3)
    proveryaem_nalichie_knopki = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").text
    assert proveryaem_nalichie_knopki, "Кнопоньки нет на месте"