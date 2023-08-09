### 튜플(Tuple) 자료형 ###

# 순서 O, 변경 X, 중복된 값의 저장 O
# 한 번 생성된 튜플은 변경이 불가능
# 소괄호()를 사용하여 생성하고, 각 요소는 쉼표(,)로 구분

# 1. Tuple 생성
tuple1 = ()  # 빈 튜플
tuple2 = (1, 2, 3)  # 정수형 튜플
tuple3 = ('a', 'b', 'c')  # 문자형 튜플
tuple4 = (1, 'a', 2.9, 'b')  # 다양한 자료형의 혼합
tuple5 = (1, 2, (3, 4))  # 튜플 안에 튜플 (중첩 튜플)

# 단일 요소(1개의 값)를 가지는 튜플을 생성할 때는 요소 뒤에 쉼표를 반드시 붙여야함
single_element_tuple = (1,)

# 2. Tuple 인덱싱 & 슬라이싱
tuple = (1, 2, 3, 4, 5)
print(tuple[1])  # 2
print(tuple[-1])  # 5

print(tuple[1:3])  # (2, 3)

# 3. Tuple 연산
# 3-1. Tuple 합치기
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)

# 3-2. Tuple 반복하기 ( * )
print(tuple1 * 2)  # (1, 2, 3, 1, 2, 3)

# 4. Tuple 관련 함수 (내장 함수)
# 4-1. 요소의 위치를 반환하는 메소드: index()
tuple = (1, 2, 3, 4)
print(tuple.index(3))  # 2

# 4-2. 주어진 값과 일치하는 요소의 개수를 반환하는 메소드: count()
tuple = (1, 2, 3, 2)
print(tuple.count(2))  # 2

# 튜플은 요소값을 변경할 수 없기 때문에 값을 변경하는 내장 함수가 없음