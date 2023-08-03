### 모듈 실습 문제 ###
# p.221

# 파이썬으로 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

# 지시사항
# 1. 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장
# 1-1. 빈 jackpot 리스트를 생성
# 2. 다음 과정을 6번 반복
# - pot 리스트를 무작위로 섞어준다 -> random 모듈의 shuffle 메서드 사용
# - pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장
# - 2초 동안 잠시 멈춤 -> time 모듈의 sleep() 메서드 사용
# 3. jackpot 리스트의 모든 요소를 오름차순 정렬
# 4. jackpot 리스트의 모든 요소 출력
# time 모듈과 random 모듈을 활용

import time
import random

pot = list(range(1, 46)) # 1.

jackpot = [] # 1-1.
for _ in range(6): # for 반복문에서 언더바 사용 시 특별히 사용되지 않는 변수 # 2.
    random.shuffle(pot)
    jackpot.append(pot.pop())
    time.sleep(2)

jackpot.sort() # 3.
print(jackpot) # 4.