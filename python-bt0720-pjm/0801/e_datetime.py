### 파이썬 표준 라이브러리 - datetime 모듈 ###
# : 날짜와 시간을 처리하는 기능
import datetime

# 현재 날짜 및 시간을 가져오기
now = datetime.datetime.now()
print(now)

# 날짜, 시간의 형식 지정
# date (날짜)
date = datetime.date(2023, 8, 1)
print(date) # 2023-08-01

# time (시간)
time = datetime.time(12, 0, 0) # 시, 분, 초
print(time) # 12:00:00

# datetime 모듈의 주요 메소드
# 오늘 날짜를 반환
print(datetime.date.today()) # 2023-08-01

# 현재 날짜와 시간을 반환
print(datetime.datetime.now()) # 2023-08-01 10:53:56.658091