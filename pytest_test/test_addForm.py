import pytest
from selenium import webdriver

inputValue = [('Diar', 'Ardiansyah', 'diar11@gmail.com', '20', '700000', 'QA')]

@pytest.fixture
def driver():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://demoqa.com/webtables')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b,c,d,e,f', inputValue)
def test_add(driver,a,b,c,d,e,f):
    driver.find_element_by_xpath('//*[@id="addNewRecordButton"]').click()
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(a)
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(b)
    driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(c)
    driver.find_element_by_xpath('//*[@id="age"]').send_keys(d)
    driver.find_element_by_xpath('//*[@id="salary"]').send_keys(e)
    driver.find_element_by_xpath('//*[@id="department"]').send_keys(f)
    enter = driver.find_element_by_xpath('//*[@id="submit"]').click()

    assert enter == None