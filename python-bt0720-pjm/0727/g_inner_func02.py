# 파이썬 내장 함수 (Built-in Function)

# 숫자형 내장 함수

# 1. abs()
# abs(x): 숫자의 절대값을 반환 (x는 정수 또는 실수)
print(abs(-5))
print(abs(3.14))

# 2. divmod()
# divmod(a, b): a를 b로 나눈 몫과 나머지를 튜플(소괄호) 형태로 반환
print(divmod(14, 4)) # (3, 2) -> 몫: 3, 나머지: 2

# 3. float() & int()
# 문자열 또는 숫자를 실수 & 정수로 변환
print(int(3.14)) # 3
print(float(3)) # 3.0

# 4. max() & min()
# max(iterable(변할 수 있는 값) 또는 max(데이터1, 데이터2, ...) 중에서 가장 큰 값을 반환
print(max([1,2,3,4,5]))
print((max(543, 24, 646, 12, 655)))

print(min([1,2,3,4,5]))
print((min(543, 24, 646, 12, 655)))

# 5. pow()
# pow(x, y): x의 y제곱한 결과를 반환
print(pow(2,3)) # 2의 3제곱 = 8

# 6. round()
# round(number(숫자), ndigits(소수점 자리숫자)): 숫자를 ndigits 소수점 자리까지 반올림한 결과를 반환
# : ndigits 생략 시 기본값은 0
print(round(3.14159, 2)) # 소수점 2번째 자리까지 출력하면서 3번째 자리에서 반올림
print(round(3.14159)) # 3

# 7. sum()
# sum(iterable, start): iterable의 모든 항목과 시작값을 더한 결과를 반환
# start 생략 시 iterable 값들만을 더한 결과를 반환 (시작값이 0)
print(sum([1,2,3,4,5])) # 15
print(sum([1,2,3,4,5], 10)) # 25 -> 10을 시작값으로 사용
