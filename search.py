import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#import sys
#sys.path.append('/usr/local/bin/phantomjs')

class LoginTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get('http://www.mytokri.com/')
        self.driver.maximize_window()

    #=================> LOGIN CHECK <=======================

    def test_from_search(self):
        fo = open("result.txt", 'a')
        start = int(time.time() * 1000)
        keyword = "book"
        self.driver.find_element_by_id("livesearch").clear()
        self.driver.find_element_by_id("livesearch").send_keys(keyword)
        self.driver.find_element_by_id("livesearchsubmit").click()
        self.driver.save_screenshot('out.png')
        title = self.driver.title
        if title.find(keyword) == 0:
            end = int(time.time() * 1000)
            fo("\nSearch Done! in " + str(end-start) + ' millisecond\n')
        else:
            fo.write("Error in searching!\n")
        fo.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
