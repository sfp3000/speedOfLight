'''
Created on Apr 6, 2017

@author: sfp300
'''
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#iepath =  "C:\saadEnvy\workspace\IEDriverServer64v3.exe"
iepath = "IEDriverServer64v3.exe"
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
 
driver.find_element_by_xpath(rubyfirstResponse).click()
time.sleep(2)
print(driver.find_elements_by_xpath(authorsXpath)[0].text)
# for elem in driver.find_elements_by_xpath(authorsXpath):
#     print (elem.text)
#print(driver.find_element_by_xpath(authorsXpath).text)
driver.quit()