### 웹 페이지 분석 및 추출하기 ###

# pip install beautifulSoup4

#! 1. BeautifulSoup 객체 생성 기본 방법

import requests
from bs4 import BeautifulSoup

url = '검색 대상 URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#! 2. BeautifulSoup 메소드 사용

#? 2-1. find() 메소드
# : 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드
# : 일반적으로 하나의 태그만 존재하는 경우에 사용