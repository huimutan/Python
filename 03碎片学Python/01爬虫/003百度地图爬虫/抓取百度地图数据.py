# coding=utf-8
# 指定编码格式，防止乱码
import requests
import time
# 百度地图API搜索
# http://api.map.baidu.com/place/v2/search?query=综合医院&region=泰安&page_size=20&page_num=0&output=json&ak=OG7q80B0WPWlkR1soVk6nWZAo8sssvTB
'''其中 query=综合医院：表示检索的poi类型为综合医院，region=泰安：表示检索区域是泰安，
page_size=20表示每一页显示20个poi点,默认为10，page_num=0表示这是第几页。
'scope': '2', 检索结果详细程度。取值为1 或空，则返回基本信息；取值为2，返回检索POI详细信息'''


def baidu_search(query, region, page_num):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'kcW2o3PQB21Fk8HEVoUhdo5mG61omxoU'  # 灰木炭
    uri = url + 'query=' + query + '&region=' + \
        region+'&output=' + output + '&ak=' + ak + \
        '&page_size=20'+'&page_num=' + str(page_num)
    r = requests.get(uri)
    response_dict = r.json()
    print(response_dict)
    # response_dict = json.loads(r.text)  # 读取JSON格式的数据
    return response_dict


not_last_page = True
page_num = 0
with open('/data.txt', 'w') as f:  # 设置文件对象
    while not_last_page:
        # time.sleep(1)
        response_dict = baidu_search('综合医院', '泰安', page_num)
        if response_dict['results']:
            for adr in response_dict['results']:
                name = adr['name']
                location = adr['location']
                lng = float(location['lng'])
                lat = float(location['lat'])
                address = adr.get('address', '不存在！')
                telephone = adr.get('telephone', '不存在！')
                print('名称：'+name+' 坐标：%f,%f' %
                      (lat, lng) + ' 地址：'+address+' 电话：'+telephone)
                f.write('名称：'+name+' 坐标：%f,%f' % (lat, lng) +
                        ' 地址：'+address+' 电话：'+telephone + '\n')  # 将字符串写入文件中
        else:
            not_last_page = False
        page_num += 1
