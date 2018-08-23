# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList?serviceKey=5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D&desc_kor={}'.format("떡볶이")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table2 = soup.find("items")
table = table2.findAll("item")
result = ""
num = 0

for i in table:
    text = table[num].findAll(text=True)
    for i in range(0,11):
        result += str(text[i*2 +1])
        i += 1
    num += 1

print(result)

# # -*- coding: utf-8 -*-
# import requests, json
# from bs4 import BeautifulSoup
# import pandas as pd
#
# url = 'http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList?serviceKey=5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D&desc_kor={}'.format("떡볶이")
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# table2 = soup.find("items")
# table = table2.findAll("item")
# view_list=['식품이름:', '1회 제공량(g):', '열량(kcal):', '탄수화물(g):', '단백질(g):','지방(g):', '당류(g):', '나트륨(g):', '콜레스테롤(g):', '포화지방산(g):', '트랜스지방산(g):']
# result = ""
# num = 0
#
# for i in table:
#     text = table[num].findAll(text=True)
#     for i in range(0,11):
#         result += view_list[i] + str(text[i*2 +1]) + '\n'
#         i += 1
#     num += 1
#
# print(result)
#
# raw_data = {'regiment': ['식품이름:', '1회 제공량(g):', '열량(kcal):', '탄수화물(g):', '단백질(g):','지방(g):', '당류(g):', '나트륨(g):', '콜레스테롤(g):', '포화지방산(g):', '트랜스지방산(g):'], 'company': result}
# df = pd.DataFrame(raw_data, columns = ['regiment', 'company'])\
#
# print(df)
# #
# #
#
#
#
# #
# headers = {
#    'ServiceKey': '5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D'
# }
# D5UeITjJnXAjZ0%2BX27g%2BjI8koefmI86tSERgKREw1dh4Ro59%2BF5C9KdrGvD9clRymrIL3PKZ33zW3d%2FT4Owihw%3D%3D
# 5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D
# 5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D
#
#
# from urllib2 import Request, urlopen
# from urllib import urlencode, quote_plus
#
# url = 'http://openapi.jbfood.go.kr:8080/openapi/service/FoodDictionaryService/getFoodDictionaryDetail'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('SNO') : '1' })
#
# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print response_body