import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://tiket.tokopedia.com/kereta-api/?ispulsa=1')
    yield driver
    driver.quit()

def test_negatif(setup):
    setup.find_element_by_xpath('//*[@data-testid="selectorAsal"]').click()
    setup.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[2]').click()
    
    error_state = setup.find_element_by_xpath('//div[@class="error-text"]').text
    assert error_state == "Stasiun keberangkatan dan tujuan tidak boleh sama."

def test_positif(setup):
    setup.find_element_by_xpath('//*[@data-testid="selectorAsal"]').click()
    setup.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[4]').click()
    setup.find_element_by_xpath('//div[@class="css-1bh52ki e4ba57s0"]').click()
    setup.find_element_by_xpath('//*[@data-testid="searchTicketButton"]').click()

    title = setup.title
    assert "Pesan Tiket Kereta Api Online" in title
    

