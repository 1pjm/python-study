# 1. 주석 (Comment)
# : 사람만 알아볼 수 있도록 설명을 작성하는 영역
# : 파이썬 인터프리터가 처리하지 않기 때문에 실행에는 영향을 미치지 않음

# 주석 활용
# : 자세한 설명을 작성 or 특정 코드를 임시로 사용하지 않도록 만들 때 사용

# 주석 처리 단축키: ctrl + /

print('주석 처리되지 않은 부분')
# print('주석 처리 된 부분')

# 1-1. 한 줄 주석
# : 샾(#) 기호를 사용하여 주석 처리
# 보통 주석 처리를 할 경우에는 코드를 읽기 쉽도록 # 뒤에 공백 한 칸을 띄움

# 1-2. 여러 줄 주석
# : (작은) 따옴표 3개로 묶어서 표현
'''
여러 줄 주석 입니다.
이 줄은 출력되지 않습니다.
'''

# 2. 세미콜론(;)
# 파이썬에서 한 줄에 여러 구문을 쓸 때는 구문과 구문 사이에 세미콜론을 붙임
# 그러나 프로그래밍에서는 한 줄에 여러 구문을 쓰지 않음
print('파이썬에서는 세미콜론 사용x'); print('세미콜론을 사용하는 경우')

# - 하이픈
# : 콜론
# & 앰퍼샌드
# ` 백틱

# 3. 들여쓰기
# : 코드를 읽기 쉽도록 일정한 간격을 띄워서 작성하는 방법
# : 파이썬에서는 들여쓰기 자체가 문법

# 3-1. 들여쓰기 방법
# : 공백(스페이스) 2칸, 4칸, 탭(tab)
# : 파이썬 코딩 스타일 가이드 - 공백 4칸으로 규정