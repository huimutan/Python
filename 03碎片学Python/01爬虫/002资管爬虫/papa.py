from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
#try:
browser.get('https://www.baidu.com')
#assert "Python" in driver.title
input = browser.find_element_by_id('kw')
input.send_keys('Python爬虫')
input.send_keys(Keys.ENTER)#Keys.RETURN
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookies())
#print(browser.page_source)
#finally:
#browser.close()
