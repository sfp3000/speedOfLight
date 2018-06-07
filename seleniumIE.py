'''
Created on Apr 6, 2017

@author: sfp300
'''
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

#############################
# loging to Facebook
#############################

urlfacebook = "https://www.facebook.com/"
fbEmailXpath = "//input[@id='email']"
fbpwdXpath = "//input[@id='pass']"
fbLoginXpath = "//input[@value='Log In']"
iepath = "IEDriverServer64v3.exe"
iepath = "IEDriverServer32.exe"
fbXpath = "//a[@class='_19eb']//span[@class='_2md']"
fbXpath = "//a[@class='_2s25' and contains(.,'Home')]"
fbXpath = ".//*[@id='js_b']/div/div/div[1]/div[1]/h1/a"

fbinputXP = "//div[@class='_1mf _1mj']"
fbpostXP = "//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']"
driver = webdriver.Ie(iepath)
driver.get(urlfacebook)
driver.maximize_window()
driver.find_element_by_xpath(fbEmailXpath).clear()
driver.find_element_by_xpath(fbEmailXpath).send_keys("sfp300@gmail.com")
driver.find_element_by_xpath(fbpwdXpath).clear()
driver.find_element_by_xpath(fbpwdXpath).send_keys("democrat")
 
driver.find_element_by_xpath(fbLoginXpath).click()
driver.implicitly_wait(5)
 
#driver.find_element_by_xpath("//a[. = 'Home']").click() 


#Facebook doesn't seem to let any scrapping. I give up.
#





url = "https://rubygems.org/"
rubyInputXpath = "//*[@id='home_query']"
rubyfirstResponse= "(//h2[contains(.,'ruby-debug19')])[1]"
authorsXpath = "/html/body/main/div/div/div[1]/div[4]/ul/li/p"

driver = webdriver.Ie(iepath)
driver.get(url = "https://rubygems.org/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_xpath(rubyInputXpath).send_keys("ruby-debug19")
 
driver.find_element_by_xpath(rubyInputXpath).send_keys(Keys.ENTER)
 
#driver.find_element_by_xpath("(//h2[contains(text(),'ruby-debug19')])[1]").click()
#driver.find_element_by_xpath("(//a[@class='gems__gem']//h2[@class='gems__gem__name'])[1]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath(rubyfirstResponse).click()



for elem in driver.find_elements_by_xpath("//div[@class='dependencies']//a[@class='t-list__item']"):
    print(elem.text)


print(driver.find_element_by_xpath(authorsXpath).text)

 
driver.quit()