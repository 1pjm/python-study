# 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
# 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현

# 돈을 입력받아서 결과 출력하는 코드
# def vending_machine():
#     money = int(input('돈: '))
#     drink = int(money) / 700 # 몇 잔
#     drink = int(drink)
#     charge = money - (drink * 700)
#     print(f'{drink}잔 뽑을 수 있습니다.')
#     print(f'잔돈은 {charge}원 입니다.')
# vending_machine()

# 함수 정의
# 반환값x
# 함수 이름: vending_machine()
# 매개변수: 정수 money

def vending_machine(money):
    drink = int(money) / 700 # 몇 잔
    drink = int(drink)
    change = money % 700
    print(f'{drink}잔의 음료수')
    print(f'잔돈 {change}원')
vending_machine(3000)

# 풀이 코드
def vending_machine(money):
    # 음료수 가격
    drink_price = 700

    # 음료수 개수 & 잔돈 계산
    num_drink = money // drink_price # 돈을 음료수 가격으로 나눈 몫(몫 구하는 연산자: //)이 음료수 개수
    change = money % drink_price # 돈을 음료수 가격으로 나눈 나머지가 잔돈

    # 출력
    print(f'{money}원을 넣었을 때: {num_drink}잔의 음료수, 잔돈 {change}원')
vending_machine(3000)