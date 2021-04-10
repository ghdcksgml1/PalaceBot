from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
url = 'https://shop.palaceskateboards.com/collections/new'
driver.get(url)

driver.maximize_window()
#driver.find_element_by_css_selector('.gLFyf.gsfi').click()

#action.send_keys('홍찬희').perform()
#action.reset_actions()

while True:
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    item = "FLY-T-SHIRT BLACK"
    count = 0
    count1 = -1
    title_list = soup.find_all('h3','title')
    for title in title_list:
        for val in title:
            count+=1
            if val==item:
                count1=count
                break
    if(count1 > -1):
        value = '//*[@id="product-loop"]/div['+str(count1)+']/div/a'    
        driver.find_element_by_xpath(value).click()
        break
    time.sleep(1)
    driver.refresh()

#사이즈선택
time.sleep(1)
element =driver.find_element_by_id("product-select")
selected = Select(element)
selected.select_by_visible_text('Medium')
driver.find_element_by_xpath('//*[@id="product-form-4921843187789"]/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="head-right"]/a').click()
time.sleep(1)
driver.find_element_by_css_selector('.checkbox-control').click()
driver.find_element_by_xpath('//*[@id="checkout"]').click()


driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('ghdcksgml2@naver.com')
checkbox = driver.find_element_by_xpath('//*[@id="checkout_buyer_accepts_marketing"]')
checkbox.click()
action = ActionChains(driver).send_keys(Keys.TAB).send_keys('hong').send_keys(Keys.TAB).send_keys('chan hee').send_keys(Keys.TAB).send_keys('123').send_keys(Keys.TAB).send_keys('456').send_keys(Keys.TAB).send_keys('789').send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys('12345').send_keys(Keys.TAB).send_keys('010-0000-0000')
action.perform()

driver.find_element_by_xpath('//*[@id="checkout_remember_me"]').click()
#driver.find_element_by_xpath('//*[@id="continue_button"]').click()

