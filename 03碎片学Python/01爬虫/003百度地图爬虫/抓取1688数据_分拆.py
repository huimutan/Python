import random
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver  # 导入selenium的浏览器驱动接口
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.keys import Keys  # 要想调用键盘按键操作需要引入keys包
# 导入chrome选项
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
# pip install msedge.selenium_tools -i https://pypi.douban.com/simple
from msedge.selenium_tools import EdgeOptions
from time import sleep
from lxml import html
import requests
import re
import time

etree = html.etree
header = {
    "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0",
    'Connection': 'close',
    "Accept-Encoding": "Gzip",
}


def get_proxy_ip_list(type=1):
    # 从快代理购买代理ip
    api_url = "https://dps.kdlapi.com/api/getdps/?orderid=980281118570139&num=20&pt=1&format=json&sep=1"
    api_url2 = "https://dps.kdlapi.com/api/getdps/?orderid=980281118570139&num=5&pt=1&format=json&sep=1"
    if type == 1:
        proxy_ip = requests.get(api_url).json()['data']['proxy_list']
    else:
        proxy_ip = requests.get(api_url2).json()['data']['proxy_list']
    return proxy_ip


def prase_urls(page_text):
    """
    解析每个页面的url，获取每个商家的网址地址，返回商家url列表
    :param page_text:
    :return:
    """
    tree = etree.HTML(page_text)
    url_list = tree.xpath(
        '//*[@id="render-engine-page-container"]/div/div[7]/div[3]/div/div/div/div[1]/div/div[1]/a/@href')
    print(url_list, len(url_list))
    return url_list


def get_page(start_url, cookies, proxy_ip):
    """
    请求商家联系方式的详情页，并返回html数据
    :param start_url:
    :param cookies:
    :param proxy_ip:
    :return:
    """
    ip = random.choice(proxy_ip)
    try:
        response = requests.get(url=start_url + '/page/contactinfo.htm', headers=header,
                                proxies={"http": ip}, cookies=cookies).text
        sleep(random.randint(1, 3))
    except Exception as e:
        response = ' '
    return {'url': url, 'text': response}


def parase_info(result):
    """
    解析商家联系方式等详细信息
    """
    res = result.result()
    page_text = res.get('text')
    try:
        if page_text:
            tree = etree.HTML(page_text)
            company_name = tree.xpath(
                '//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/h4/text()')
            company_member_name = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div['
                                             '1]/dl/dd//text()')
            compang_phone = tree.xpath(
                '//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/dl[1]/dd/text()')
            compang_mobilephone = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div['
                                             '2]/dl[2]/dd/text()')
            year = tree.xpath('//*[@id="site_content"]/div[2]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/span['
                              '1]/a/span/span/text()|//*[@id="site_content"]/div[2]/div/div/div[2]/div/div/div['
                              '1]/div[1]/div[2]/a/span/text()')

            if len(company_name) > 0:
                company_name = company_name[0]
                company_member_name = company_member_name[1] + \
                    ''.join(company_member_name[2].split())
                # year = year[0]
                rule = re.compile(r'^\d')
                if len(compang_mobilephone) > 0:
                    compang_mobilephone = compang_mobilephone[0].strip(
                        ' ').strip('\n')
                    if rule.match(compang_mobilephone[0:1]) is None:
                        compang_mobilephone = ''
                else:
                    compang_mobilephone = ''

                if len(compang_phone) > 0:
                    compang_phone = compang_phone[0].strip(' ').strip('\n')
                    if rule.match(compang_phone[0:1]) is None:
                        compang_phone = ''
                else:
                    compang_phone = ''
                if len(compang_mobilephone) > 0 or len(compang_phone) > 0:
                    # print('%s|%s|%s|%s|%s' % (
                    #     company_name, company_member_name, compang_mobilephone, compang_phone, year[0]))
                    with open('%s.txt' % keyword, 'a', encoding='utf-8') as f:
                        f.write('%s|%s|%s|%s|%s\n' % (
                            company_name, company_member_name, compang_mobilephone, compang_phone, year[0]))
                    print('%s|%s|%s|%s|%s' % (
                        company_name, company_member_name, compang_mobilephone, compang_phone, year[0]))
    except Exception as e:
        print(e)


# 搜索关键词
keyword = '四件套'
# 搜索省份 城市
area = {'province': '湖北', 'page': 19}
url = 'https://www.1688.com/'
# auto_login(area, keyword, url)
# def auto_login(area, keyword, url):
"""
:param area:
:param keyword:
:param url:
:return:
扫码登陆阿里巴巴账号
"""
province = area['province']
page = area['page']
options = EdgeOptions()  # option = ChromeOptions()
options.add_argument('--headless')  # 创建chrome浏览器驱动，无头模式（超爽）
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Edge(
    executable_path=r'D:\02Run\edgedriver_win64\msedgedriver.exe')
# driver = webdriver.Edge(r'D:\02Run\edgedriver_win64\msedgedriver.exe')
driver.get(url)
driver.implicitly_wait(10)  # 隐性等待，最长等10秒
sleep(1)
# driver.find_element_by_xpath(
# '//*[@id="alibar"]/div[1]/div[2]/ul/li[3]/a').click()
driver.find_element_by_xpath("//a[@class='user_login']").click()
driver.implicitly_wait(20)
driver.switch_to.frame(driver.find_element_by_xpath(
    '//*[@id="loginchina"]/iframe'))
sleep(2)
# 选择扫码登录,可以拿手机直接扫selenium打开的网站 等待时间8秒，2秒后刷新网站，等待三秒等网站刷新
driver.find_element_by_xpath('//div[@id="login"]/div[1]/i').click()
# driver.find_element_by_xpath("//input[@id='tuiguangServer']").click()
sleep(12)
driver.refresh()
driver.implicitly_wait(10)
sleep(4)
# 选择搜索关键词
driver.find_element_by_xpath(
    '//input[@id="home-header-searchbox"]').send_keys(keyword)
    #"//div[@class='alisearch-action']/button").click()
driver.find_element_by_xpath(
    " //div[@class='header-searchbox']//button[@class='single']").click()
sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 选择供应商
# driver.find_element_by_xpath(
    # '//*[@id="render-engine-page-container"]/div/div[2]/div/div[3]/div[1]/div/span[3]/a/span').click()#点击工业品牌
driver.find_element_by_xpath("//div[@class='mainTab-container']//span[3]//a[1]//span[1]").click()
sleep(2)
print('------------------%s资料开始爬取------------------' % province)
# area = driver.find_element_by_xpath("//*[@id='sw_mod_filter_area']")
area = driver.find_element_by_xpath(
    '//*[@id="render-engine-page-container"]/div/div[6]/div[1]/div[1]')
ActionChains(driver).move_to_element(area).perform()
# province_button = driver.find_element_by_link_text(province)
# ActionChains(driver).move_to_element(province_button).perform()
# driver.find_element_by_link_text(city).click()
# 阿里巴巴前端更新 这个是城市选择湖北
driver.find_element_by_xpath(
    '//*[@id="render-engine-page-container"]/div/div[6]/div[1]/div[2]/ul[2]/li[16]').click()
driver.implicitly_wait(10)
sleep(1)
count = 1
# driver.find_element_by_xpath('//*[@id="jumpto"]').send_keys(count)
# sleep(0.5)
# driver.find_element_by_xpath('//*[@id="jump-sub"]').click()
# driver.implicitly_wait(10)
start_time = time.time()
proxy_ip = get_proxy_ip_list(type=1)
while count <= page:
    print('------------正在爬取%s第%s页数据------------' % count)
    count += 1
    driver.execute_script(
        'window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });')
    driver.implicitly_wait(10)
    page_text = driver.page_source
    sleep(random.uniform(2.1, 5.0))
    executor = ThreadPoolExecutor(5)
    urls_list = prase_urls(page_text)

    c = driver.get_cookies()
    cookies = {}
    # 获取cookie中的name和value,转化成requests可以使用的形式
    for cookie in c:
        cookies[cookie['name']] = cookie['value']
    for detail_url in urls_list:
        executor.submit(get_page, detail_url, cookies,
                        proxy_ip).add_done_callback(parase_info)
    executor.shutdown(wait=True)
    if page > 1:
        driver.find_element_by_xpath(
            '//*[@id="render-engine-page-container"]/div/div[8]/div/div/div/span[2]/input').clear()
        driver.find_element_by_xpath(
            '//*[@id="render-engine-page-container"]/div/div[8]/div/div/div/span[2]/input').send_keys(count)
        sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="render-engine-page-container"]/div/div[8]/div/div/div/span[3]/button').click()
        driver.refresh()
        end_time = time.time()
        # 每六十秒向代理池加入新的ip
        if end_time - start_time > 60:
            proxy_ip += get_proxy_ip_list(type=2)

else:
    print('------------%s资料已爬取完毕------------')
    print('-------------------------------------------')
print('------------------所有资料已爬取完毕------------------')
