import unittest
from selenium import webdriver
import time


class Error404Check(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get('http://www.mytokri.com/')
        self.driver.maximize_window()

    #==================> 404 Checking <====================

    def test_from_check404(self):
        error404 = "MyTokri - 404 Error Page"
        error404 = error404.lower()
        links = self.driver.find_elements_by_xpath("//*[@href]") #links array with href
        urls = []
        for element in links:
            link = element.get_attribute("href")
            url = str(link)
            if (url.find('http://www.mytokri.com/') != -1):
                urls.append(url)

        print len(urls)
        error = 0
        for url in urls:
            self.driver.get(url)
            title = self.driver.title
            try:
                title = str(title).lower()
                if (title.find(error404) == -1):
                    print "Correct URL - " + url
                    continue
                else:
                    error = error + 1
                    print "Error at URL - " + url
            except UnicodeEncodeError:
                pass
        print "Total 404 Error in HomePage- " + str(error)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
