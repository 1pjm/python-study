### 파이썬 표준 라이브러리 - os 모듈 ###
# : operate system(운영 체제)와 상호작용하는 기능

import os

# 현재 작업 디렉토리(폴더) 확인
print(os.getcwd()) # C:\python-bt0720-pjm\0801

# 디렉토리 생성
# os.mkdir('practice02')

# 디렉토리 확인
print(os.listdir())

# 디렉토리 삭제
# os.rmdir('practice02')
# 삭제하려는 디렉토리가 존재하지 않을 경우 오류가 발생