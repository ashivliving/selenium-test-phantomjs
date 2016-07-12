import unittest
from selenium import webdriver
import time
#import sys
#sys.path.append('/usr/local/bin/phantomjs')

class LoginTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        self.driver.get('http://www.mytokri.com/')
        self.driver.maximize_window()

    #=================> LOGIN CHECK <=======================

    def test_from_login(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div/div/a[6]").click()
        time.sleep(2)
        self.driver.find_element_by_id("ctrl_pageLogin_login").clear()
        self.driver.find_element_by_id("ctrl_pageLogin_login").send_keys("rachitamishra10.rm@gmail.com")
        self.driver.find_element_by_id("ctrl_pageLogin_password").clear()
        self.driver.find_element_by_id("ctrl_pageLogin_password").send_keys("rachita10")
        if self.driver.find_element_by_id("ctrl_pageLogin_remember").is_selected():
            self.driver.find_element_by_id("ctrl_pageLogin_remember").click()
        self.driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # driver.save_screenshot('out.png')
        print "Login Successful!"

    #=======================> Check Title <============================

    def test_from_title(self):
        print self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
