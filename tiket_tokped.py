from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://tiket.tokopedia.com/kereta-api/?ispulsa=1')

driver.maximize_window()

# pilih tempat berangkat
driver.find_element_by_xpath('//*[@data-testid="selectorAsal"]').click()

driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[5]').click()

# pilih tanggal pulang 
driver.find_element_by_xpath('//div[@class="css-1bh52ki e4ba57s0"]').click()
driver.find_element_by_xpath('//*[@data-testid="selectorPulang"]').click()
driver.find_element_by_xpath('//*[@data-testid="date20211219"]').click()

# click save 
driver.find_element_by_xpath('//button[@class="css-1ftsx1j-unf-btn e1ggruw00"]').click()
driver.find_element_by_xpath('//*[@data-testid="searchTicketButton"]').click()

