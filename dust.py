import requests
from pprint import pprint

URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

res = requests.get(URL)

data = res.json()

items = data['response']['body']['items'] #response 안의 body 안의 items을 가져오는 것

for item in items:
    if item['stationName'] == '강남구':
        pprint(item['pm10Value']) #item안에 원하는 값에 접근하는 방법