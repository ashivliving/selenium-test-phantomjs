from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get('http://www.mytokri.com')
driver.maximize_window()
#driver.save_screenshot('out.png');
#===============> For Getting Title <=====================
print driver.title
#===============> For Login Check <======================
time.sleep(1)
driver.find_element_by_xpath("/html/body/header/div/div/div/div/a[6]").click()
time.sleep(2)
driver.find_element_by_id("ctrl_pageLogin_login").clear()
driver.find_element_by_id("ctrl_pageLogin_login").send_keys("rachitamishra10.rm@gmail.com")
driver.find_element_by_id("ctrl_pageLogin_password").clear()
driver.find_element_by_id("ctrl_pageLogin_password").send_keys("rachita10")
if driver.find_element_by_id("ctrl_pageLogin_remember").is_selected():
    driver.find_element_by_id("ctrl_pageLogin_remember").click()
driver.find_element_by_css_selector("input.btn.btn-primary").click()
#driver.save_screenshot('out.png')
print "Login Successful!"
driver.quit()