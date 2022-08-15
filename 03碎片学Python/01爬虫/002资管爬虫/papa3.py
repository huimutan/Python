from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#import time  

# from selenium.webdriver.chrome.options import Options  
# __browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址  
# chrome_options = Options()  
# chrome_options.binary_location = __browser_url  
# browser = webdriver.Chrome(chrome_options=chrome_options)

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://10.213.51.39:7019/irms/jsp/login.jsp')  #家客业务支撑
wait = WebDriverWait(browser, 5)
browser.find_element_by_id("useraccount_field").send_keys("liukaita" + Keys.RETURN)  
browser.find_element_by_id("password").send_keys("Ta666666" + Keys.RETURN)  
#验证码
browser.get('http://10.213.51.39:7019/irms/jsp/resource/sdresource/hbo/tools/allLinkError.jsp')#账号重新激活 
#browser.find_element_by_id("ext-gen66")

#<input type="text" size="24" autocomplete="off" id="cityCombo" name="cityCombo" class="x-form-text x-form-field x-form-invalid x-form-focus" style="width: 183px;">
#browser.find_element_by_id("ext-gen70").send_keys(Keys.RETURN) #下拉按钮
browser.find_element_by_id("cityCombo").send_keys("泰安"+ Keys.RETURN)
wait = WebDriverWait(browser, 3)
browser.find_element_by_css_selector(".x-combo-selected").click()
#select = Select(browser.find_element_by_id("cityCombo")) #所属地市
#select.select_by_visible_text("泰安")

#<input type="text" size="20" autocomplete="off" id="account" name="account" class="x-form-text x-form-field" style="width: 150px;">
browser.find_element_by_id("account").clear() #清除
browser.find_element_by_id("account").send_keys("13685481221" + Keys.RETURN) #账号
browser.find_element_by_id('ext-gen36').send_keys(Keys.RETURN) #点击"查询"按钮 提交搜索请求
wait = WebDriverWait(browser, 3)

browser.find_element_by_id("account").clear() #清除
browser.find_element_by_id("account").send_keys("15269804153" + Keys.RETURN) 
browser.find_element_by_id('ext-gen36').send_keys(Keys.RETURN) #点击"查询"按钮 提交搜索请求 
wait = WebDriverWait(browser, 3)

#("x-grid3-cell-inner x-grid3-col-3")("x-grid3-col x-grid3-cell x-grid3-td-3")
browser.find_element_by_css_selector('.x-grid3-col').click()
browser.find_element_by_link_text('HSI').click()#——定位文字连接好用
browser.find_element_by_partial_link_text('HSI').click()#——定位文字连接好用
browser.find_element_by_xpath("HSI").click()

""" #WebDriver 中提供了一个叫 Select 的方法,可以根据索引来选择，可以根据值来选择，可以根据文字来选择。是十分方便的
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
#全部取消选择
select = Select(browser.find_element_by_id('id'))
select.deselect_all()
#获取所有的已选选项
select = Select(browser.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options
#提交
driver.find_element_by_id("submit").click()
"""

wait = WebDriverWait(browser, 10)
#wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
#time.sleep(3)  
#browser.quit()  


import pandas as pd
import numpy as np
from datetime import datetime
from pandas import Series, DataFrame

df = pd.read_excel('/ceshi.xlsx')# (input_file, sheetname='Sheet1')#读取测试文件的Sheet1   
#df = pd.read_excel(r'E:\工作文件\周报\周数据\测试\0902-0908\an-商品汇总-uv.xls')
df.columns
df.head(5) #前5行
#df.loc[0:3] #按标签提取,0-3行
#df.iloc[[0,2,5],[4,5]] #[0, 2, 5] 代表指定的行，[ 4, 5 ] 代表指定的列
#df.iloc[:2, :1]#loc——通过行标签索引行数据, iloc——通过行号索引行数据 

writer = pd.ExcelWriter('/ceshi.xlsx')#先定义写入的文件名('D:/11File/ceshi.xlsx')
#data_frame1 = pd.DataFrame(data={'col2':[1,5], 'col3':[2,4]})
df.ix[0,'输出']='222'
#df.ix['col2','l2']=10
df.to_excel(writer, sheet_name='Sheet1')#表1写入sheet1
writer.save()#写完后保存




