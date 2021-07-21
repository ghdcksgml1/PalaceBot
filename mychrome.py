# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import time
from tkinter import *
from tkinter import filedialog as fd
import tkinter.font as tkFont
import tkinter.ttk as ttk

driver = ""
C_driv = ""


def search():
    global driver
    # 크롬 실행
    driver = webdriver.Chrome(C_driv)
    driver.get('https://shop.palaceskateboards.com/collections/new')
    driver.maximize_window()  # 윈도우화면 최대화


def start():
    global driver
    item = r1.get().upper()
    size = r2.get()  # 리스트
    email = r3.get()  # 텍스트
    firstname = r4.get()  # 텍스트
    lastname = r5.get()  # 텍스트
    address = r6.get()  # 텍스트
    apartment = r7.get()  # 텍스트
    city = r8.get()  # 텍스트
    postcode = r9.get()  # 텍스트
    phone = r10.get()  # 텍스트
    # new카테고리에서 원하는 아이템을 가져오는 과정, 찾을때 까지
    while True:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        count = 0
        count1 = -1
        title_list = soup.find_all('h3', 'title')
        for title in title_list:
            for val in title:
                count += 1
                if val == item:
                    count1 = count
                    break
        if(count1 > -1):
            value = '//*[@id="product-loop"]/div['+str(count1)+']/div/a'
            driver.find_element_by_xpath(value).click()
            break
        time.sleep(1)
        driver.refresh()
    # 사이즈선택 후 카트에 담기
    time.sleep(1)
    element = driver.find_element_by_id("product-select")
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
    checkbox = driver.find_element_by_xpath(
        '//*[@id="checkout_buyer_accepts_marketing"]')
    checkbox.click()
    action = ActionChains(driver).send_keys(Keys.TAB).send_keys(firstname).send_keys(Keys.TAB).send_keys(lastname).send_keys(Keys.TAB).send_keys(address).send_keys(
        Keys.TAB).send_keys(apartment).send_keys(Keys.TAB).send_keys(city).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(postcode).send_keys(Keys.TAB).send_keys(phone)
    action.perform()
    driver.find_element_by_xpath('//*[@id="checkout_remember_me"]').click()


# Tkinter
window = Tk()
# window.iconbitmap(default='C:/Education/PalaceBot/palace-skateboards.ico')
window.title("PALACE BOT")
window.geometry("700x500+100+100")
window.resizable(False, False)

# 제목
labelfont = tkFont.Font(family="Lucida Grande", size=20)
label = Label(window, text="PALACE BOT", font=labelfont)
label.grid(row=0, column=1, ipady=20)


# 레이블들
anotherLabelFont = tkFont.Font(size=10)
Label(window, text="i t e m", font=anotherLabelFont).grid(row=1, ipadx=30)
Label(window, text="s i z e", font=anotherLabelFont).grid(row=2)
Label(window, text="e m a i l", font=anotherLabelFont).grid(row=3)
Label(window, text="first name", font=anotherLabelFont).grid(row=4)
Label(window, text="last name", font=anotherLabelFont).grid(row=5)
Label(window, text="address", font=anotherLabelFont).grid(row=6)
Label(window, text="apartment", font=anotherLabelFont).grid(row=7)
Label(window, text="c i t y", font=anotherLabelFont).grid(row=8)
Label(window, text="post code", font=anotherLabelFont).grid(row=9)
Label(window, text="p h o n e", font=anotherLabelFont).grid(row=10)
Label(window, text="Chrome_Driver 경로 :  ",
      font=anotherLabelFont).grid(row=13, column=0)
#Label(window, text=)

# 엔트리들
rwidth = 50

r1 = Entry(window, width=rwidth)
r1.grid(row=1, column=1)
r2 = ttk.Combobox(window, values=[
                  "Small", "Medium", "Large", "X-Large", "One Size"], width=rwidth-3, state="readonly")
r2.current(1)
r2.grid(row=2, column=1)
r3 = Entry(window, width=rwidth)
r3.grid(row=3, column=1)
r4 = Entry(window, width=rwidth)
r4.grid(row=4, column=1)
r5 = Entry(window, width=rwidth)
r5.grid(row=5, column=1)
r6 = Entry(window, width=rwidth)
r6.grid(row=6, column=1)
r7 = Entry(window, width=rwidth)
r7.grid(row=7, column=1)
r8 = Entry(window, width=rwidth)
r8.grid(row=8, column=1)
r9 = Entry(window, width=rwidth)
r9.grid(row=9, column=1)
r10 = Entry(window, width=rwidth)
r10.grid(row=10, column=1)

C_driv = fd.askopenfilename()
# 버튼
b0 = Button(window, text="조회", command=search,
            font=anotherLabelFont).grid(row=11, column=0)
b1 = Button(window, text="시작", command=start,
            font=anotherLabelFont).grid(row=11, column=1)
#b2 = Button(window,text="종료",command=window.quit)

Label(window, text=C_driv, font=anotherLabelFont).grid(row=13, column=1)
window.mainloop()
