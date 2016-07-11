from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get('http://www.mytokri.com')
driver.maximize_window()
#============> Check 404 on everypage <============
links = driver.find_elements_by_xpath("//*[@href]")
print len(links)
driver.quit()