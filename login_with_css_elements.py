from splinter import Browser   #import splinter , if you don't have then install by pip install splinter
from selenium import webdriver #import selenium web driver

webdriver_chrome=webdriver.Chrome('/Users/exepaul/Downloads/chromedriver/chromedriver')   #path of your downloaded webdriver
browser=Browser('chrome')
visit_url=browser.visit('https://www.facebook.com')   #url of website

login_field='input[type="email"]'
find_login_field=browser.find_by_css(login_field)
find_login_field.fill("example@gmail.com")  #replace example@gamil.com with your email-id
password_field='input[type="password"]'
find_password_field=browser.find_by_css(password_field)
find_password_field.fill("example12345")    #replace example12345 with your password

submit_button='label[class="uiButton uiButtonConfirm"]'
submit_button_find=browser.find_by_css(submit_button)
submit_button_find.click()

