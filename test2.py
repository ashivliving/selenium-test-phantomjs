from selenium import webdriver
import time

driver = webdriver.PhantomJS()

start = int(time.time() * 1000)
driver.get('http://www.mytokri.com')
print driver.title
end = int(time.time() * 1000)
print 'Time Taken to load page - ' + str(end-start) + 'millisecond'
#element = driver.find_element_by_xpath('/html/body')
#print element.text