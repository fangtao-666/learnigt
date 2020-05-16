from selenium import webdriver
import time
import requests

driver = webdriver.Firefox()
driver.get('https://wenku.baidu.com/view/9a5a21cf964bcf84b9d57bea?pn=50')
for i in range(50):
    if i == 3:
        target = driver.find_element_by_id('html-reader-go-more')
        driver.execute_script("arguments[0].scrollIntoView();", target)
        button = driver.find_element_by_xpath("//p[@class='down-arrow goBtn']")
        button.click()
        time.sleep(2)
    page = 'pageNo-' + str(i+1)
    print(page)
    target = driver.find_element_by_id(page)
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(2)
    mystring = driver.page_source;
    idx1 = mystring.find('<div class="bd" id="' + page)
    print(idx1)
    mystring = mystring[idx1:]
    idx1 = mystring.find("https")
    print(idx1)
    idx2 = mystring.find(");background-position")
    print(idx2)
    mystring = mystring[idx1:idx2]
    mystring = mystring.replace('amp;', '')
    if mystring.startswith('http') :
        r = requests.get(mystring)
        with open(page + '.png', 'wb') as png:
            png.write(r.content)
        png.close()
    else:
        print(mystring)

driver.get('https://wenku.baidu.com/view/9a5a21cf964bcf84b9d57bea?pn=51')
for i in range(50,66):
    page = 'pageNo-' + str(i + 1)
    print(page)
    target = driver.find_element_by_id(page)
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(2)
    mystring = driver.page_source;
    idx1 = mystring.find('<div class="bd" id="' + page)
    print(idx1)
    mystring = mystring[idx1:]
    idx1 = mystring.find("https")
    print(idx1)
    idx2 = mystring.find(");background-position")
    print(idx2)
    mystring = mystring[idx1:idx2]
    mystring = mystring.replace('amp;', '')
    if mystring.startswith('http'):
        r = requests.get(mystring)
        with open(page + '.png', 'wb') as png:
            png.write(r.content)
        png.close()
    else:
        print(mystring)
driver.quit()
