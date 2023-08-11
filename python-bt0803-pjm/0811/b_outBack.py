### 아웃백 스테이크 하우스 웹 페이지의 header 태그 추출 ###

import requests
from bs4 import BeautifulSoup

url = 'https://www.outback.co.kr/menu/productView.do?cateIdx=49&pdtIdx=10314&menuIdx=43'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

id_element = soup.find(id='dHead')
print(id_element)
print(id_element.text)
