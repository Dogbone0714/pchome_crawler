import requests
import json  #pchome 資料型態為json
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E7%AD%86%E9%9B%BB&page=1&sort=sale/dc"
res = requests.get(url) #Request Method: GET
data = json.loads(res.text)
webdatas = data ['prods'] #提出prods 類別到 webdatas
for product in webdatas :
    print (product['name'])
    print (product['price'])
