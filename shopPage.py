from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://www.tokopedia.com/unilever')

# skip coachmark 
driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-64apm5 ety06v15"]').click()

# input produck name
inputProductName = driver.find_element_by_xpath('//input[@class="css-ubsgp5 e16vycsw0"]')
inputProductName.send_keys('ponds')

# click button search 
driver.find_element_by_xpath('//button[@class="css-1czin5k e1v0ehno1"]').click()

# click product 
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@data-testid="master-product-card"]').click()

# click share
shareProduct = driver.find_element_by_xpath('//*[@data-testid="pdpShareButton"]')
shareProduct.click()

# share with copy link 
driver.find_element_by_xpath('//*[@data-testid="btnTwitterShare"]').click()