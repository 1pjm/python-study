# 학생 - 사람의 클래스를 상속관계로 구현 #

# super() 함수
# : 자식 클래스에서 부모 클래스의 메소드나 속성에 접근하기 위해 사용

class Person: # 슈퍼 클래스
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '이(가) ' + food + '을(를) 먹습니다.')

class Student(Person): # 서브 클래스
    def __init__(self, name, school):
        super().__init__(name) # 부모 클래스의 __init__ 메소드 호출
        self.school = school

    def study(self):
        print(self.name + '은(는) ' + self.school + '에서 공부를 합니다.')

jimin = Student('박지민', '와플대학교')
jimin.eat('아이스크림')
jimin.study()

junGook = Person('이준국')
junGook.eat('초콜릿')