### 객체 & 클래스 정의 ###

#! 1. 객체란?
# 서로 많은 데이터를 하나로 묶어서 표현한 것

# ex) 웹 페이지에 작성할 게시글
# : 게시글 번호, 작성자, 제목, 내용, 작성일자, 수정일자, ...

#! 2. 클래스란?
# 객체를 만드는 도구

# ex) 붕어빵(객체) & 붕어빵 틀(클래스)
#     와플(객체) & 와플 머신(클래스)
# : 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있음

#! 3. 인스턴스란?
# 클래스를 이용해서 생성한 객체를 가리키는 용어
# ex) 와플 머신(클래스)으로 만든 와플은 객체(object)
#     와플은 와플 머신(클래스)으로 만든 인스턴스(instance)
# 객체 = 인스턴스

# 객체 / 클래스
# 박지민 / 사람
# 신라면 / 라면

# 클래스 / 객체
# 자동차 / 포르쉐
# 프로그래밍언어 / 파이썬

#! 4. 클래스 정의
# : 클래스를 생성
# - class 키워드로 클래스를 정의
# - 클래스 이름은 Upper Camel Case 규칙을 따름

# ? 파이썬 명명 규칙
# 변수, 함수, 파일명: snake_case (ex: my_best_friend)
# 클래스: Upper Camel Case

# UpperCamelCase: 첫 글자 & 이어지는 단어의 첫 글자를 대문자로 작성
# (ex: MyBestFriend)
# lowerCamelCase: 이어지는 단어의 첫 글자만 대문자로 작성
# (ex: myBestFriend)

# ? 클래스 기본 형식 - 들여쓰기 문법을 따름
# class 클래스명:
#     본문 (클래스 상세정의)

#! 5. 객체 생성
# 객체명 = 클래스()
# 객체1 = 클래스()
# 객체2 = 클래스()

#! 6. 클래스 정의와 객체 생성
class WaffleMachine:
    pass  # 아무런 정의 없이 클래스를 생성


waffle = WaffleMachine()
# waffle (객체), WaffleMachine (클래스)
print(waffle)
# <__main__.WaffleMachine object at 0x00000242DEAA7750>
# : 0x00000242DEAA7750 주소에 저장된 WaffleMachine 객체