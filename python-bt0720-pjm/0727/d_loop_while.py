# 1.
# while문: 사용자로부터 숫자를 계속 입력받다가
# , 사용자가 0을 입력하면 프로그램이 종료되는 프로그램 작성
while True: # 무한루프 생성 -> while True
    num = int(input('숫자 입력(0을 입력하면 종료): '))
    if num == 0:
        break
