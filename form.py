from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://demoqa.com/automation-practice-form')

driver.maximize_window()

# input first name
inputName = driver.find_element_by_xpath('//input[@id="firstName"]')
inputName.send_keys('Diar')

# input last name
inputName2 = driver.find_element_by_xpath('//input[@id="lastName"]')
inputName2.send_keys('Ardiansyah')

# input email user
emailInput = driver.find_element_by_xpath('//input[@id="userEmail"]')
emailInput.send_keys('ardiansyahdiar@gmail.com')
