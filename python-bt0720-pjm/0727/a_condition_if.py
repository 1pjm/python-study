# 1.
# (교과서) if문: 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요.
# 관계 연산자, 논리 연산자
num1 = int(input('첫번째 숫자: ')) # input 입력값 문자열로 인식 -> int 형변환 필요
num2 = int(input('두번째 숫자: '))
num3 = int(input('세번째 숫자: '))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print('가장 큰 수는', largest, '입니다.')

# 2.
# (교과서) if문: 미세먼지 저감 활동의 일환으로 차량 2부제 실시
# 사용자로부터 차량번호를 입력받아 차량번호가 짝수로 끝나면 '운행가능'
# , 아니면 '운행불가'를 출력하는 프로그램을 구현하세요.
# 단, 차량번호는 '237가 1234'와 같은 형식으로 입력받는다고 가정합니다.

number = input('차량번호(예: 237가 1234): ')

# 입력 받은 차량번호에서 마지막 숫자를 추출
last_digit = int(number[-1]) # 인덱스 뒤에서부터 추출(뒤에서 1번째), 문자열이므로 숫자로 변환
if last_digit % 2 == 0:
    print('운행가능')
else:
    print('운행불가')