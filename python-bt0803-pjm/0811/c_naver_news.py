### 네이버 뉴스 헤드라인 크롤링 ###

import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/030/0003124590?sid=105'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

headline = soup.select('.media_end_head_headline')
print(headline)
