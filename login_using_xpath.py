from splinter import Browser   #import splinter , if you don't have then install by pip install splinter
from selenium import webdriver #import selenium web driver 

webdriver_chrome=webdriver.Chrome('/Users/exepaul/Downloads/chromedriver/chromedriver')   #path of your downloaded webdriver 
browser=Browser('chrome')
visit_url=browser.visit('https://www.facebook.com')   #url of website

login_field='//*[@id="email"]'                         
find_login=browser.find_by_xpath(login_field)   
find_login.fill("example@gmail.com")                  #replace example@gamil.com with your email-id
password_field='//*[@id="pass"]'
find_password=browser.find_by_xpath(password_field)
find_password.fill('example12345')                    #replace example12345 with your password

login_button='//*[@id="loginbutton"]'
login_button_find=browser.find_by_xpath(login_button)
login_button_find.click()

#done
