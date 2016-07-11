from selenium import webdriver
import time
driver = webdriver.PhantomJS()
baseUrl = "http://www.mytokri.com/"
driver.get(baseUrl)
driver.maximize_window()
#============> Check 404 on everypage <============
error404 = "MyTokri - 404 Error Page "
error404 = error404.lower()
links = driver.find_elements_by_xpath("//*[@href]")
urls = []
for element in links:
    link =  element.get_attribute("href")
    url = str(link)
    if (url.find(baseUrl) != -1):
        urls.append(url)

print len(urls)
error = 0
for url in urls:
    driver.get(url)
    title = driver.title
    try:
        title = str(title).lower()
        if (title.find(error404) == -1):
            #print "Correct URL - " + url
            continue
        else:
            error = error + 1
            print "Error at URL - " + url
    except UnicodeEncodeError:
        pass
print "Total 404 Error in HomePage- "+ error
driver.quit()