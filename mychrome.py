from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import time

url = 'https://shop.palaceskateboards.com/collections/new' #텍스트
item = "FLY-T-SHIRT ORANGE" # 텍스트
size = 'X-Large' # 리스트
email ='ghdcksgml2@naver.com' # 텍스트
firstname='hong' # 텍스트
lastname='chan hee' # 텍스트
address='123' # 텍스트
apartment='456' # 텍스트
city='789' # 텍스트
postcode='12345' # 텍스트
phone='010-0000-0000' # 텍스트

# 크롬 실행
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
driver.get(url)
# 윈도우화면 최대화
driver.maximize_window()
#driver.find_element_by_css_selector('.gLFyf.gsfi').click()

#action.send_keys('홍찬희').perform()
#action.reset_actions()

# new카테고리에서 원하는 아이템을 가져오는 과정, 찾을때 까지
while True:
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

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
# 사이즈선택 후 카트에 담기
time.sleep(1)
element =driver.find_element_by_id("product-select")
selected = Select(element)
selected.select_by_visible_text(size)
driver.find_element_by_css_selector('.add.cart-btn.clearfix').click()
time.sleep(1.5)
# 카트에 들어가 결제 창 들어가기
driver.find_element_by_css_selector('.cart-heading').click()
time.sleep(1)
driver.find_element_by_css_selector('.checkbox-control').click()
driver.find_element_by_xpath('//*[@id="checkout"]').click()
# 주소 입력창에 주소정보 입력
driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys(email)
checkbox = driver.find_element_by_xpath('//*[@id="checkout_buyer_accepts_marketing"]')
checkbox.click()
action = ActionChains(driver).send_keys(Keys.TAB).send_keys(firstname).send_keys(Keys.TAB).send_keys(lastname).send_keys(Keys.TAB).send_keys(address).send_keys(Keys.TAB).send_keys(apartment).send_keys(Keys.TAB).send_keys(city).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(postcode).send_keys(Keys.TAB).send_keys(phone)
action.perform()

driver.find_element_by_xpath('//*[@id="checkout_remember_me"]').click()
#driver.find_element_by_xpath('//*[@id="continue_button"]').click()

