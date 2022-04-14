from lib2to3.pgen2 import driver
import time
import pytest 
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


pencarian = [('ponds')]

@pytest.fixture
def setup():
    ser = Service('C://chromedriver_win32/chromedriver')
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://www.tokopedia.com/unilever')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a',pencarian)
def test_shopPage(setup,a):
    setup.find_element(By.XPATH, '//*[@data-testid="btnAknowledgeHyperlocalCoachmark"]').click()
    setup.find_element(By.XPATH, '//input[@class="css-ubsgp5 e16vycsw0"]').send_keys(a)
    setup.find_element(By.XPATH, '//button[@class="css-1czin5k e1v0ehno1"]').click()
    setup.find_element(By.XPATH, '//*[@data-testid="master-product-card"]').click()
    setup.find_element(By.XPATH, '//*[@data-testid="pdpShareButton"]').click()
    setup.find_element(By.XPATH, '//*[@data-testid="btnCopyShare"]').click()

    time.sleep(2)
    toaster = setup.find_element(By.XPATH, '//div[@class="css-1xfo2xm-unf-toaster eqno0ef0"]').text
    assert 'Tautan berhasil di salin' in toaster
