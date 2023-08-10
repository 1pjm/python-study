import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/'
params = {'lt': '1&ft=0'}
response = requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

# CGV 영화 예매 사이트 - 메인 페이지 무비 차트의 영화 제목을 가져오기
# class: movieName

class_elements = soup.find_all(class_='skipnaiv')
for element in class_elements:
    print(element)


# url = 'https://www.cgv.co.kr/'
# params = {
#     'NaPm': 'ct%3Dll4ivabo%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3Dnull%7Chk%3Dc0553a03d83441e24a0d30b7aa52927eff1b7e42'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
# }
# response = requests.get(url, params=params, headers=headers)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')

# # CGV 영화 예메 사이트 - 메인 페이지 무비 차트의 영화 제목을 가져오기
# # class: movieName

# class_elements = soup.find_all('div', class_='movieName')
# for element in class_elements:
#     print(element) # SSLError 보안코드 오류 사이트 접근 불가