### 객체 지향 프로그램 도입의 필요성 ###

# 학생 정보를 전달하는 student_info() 함수
# 이름, 학년, 반, 전화번호, 주소, 성적

def student_info(name, grade, class_number, phone_number, address, score):
    # 학생정보를 print()로 출력
    # VS Code 기능: alt + shift + 방향키
    print(name)
    print(grade)
    print(class_number)
    print(phone_number)
    print(address)
    print(score)


# student_info() 함수를 사용하여 학생1을 생성
name1 = 'Park Ji Min'
grade1 = 3
class_number1 = 2
phone_number1 = "010-1111-2222"
address = "부산시 동래구"
score = 90

student_info(name1, grade1, class_number1, phone_number1, address, score)

# 클래스를 이용한 학생 관리 #


class Student:
    def __init__(self, name, grade, class_number, phone_number, address, score):
        self.name = name
        self.grade = grade
        self.class_number = class_number
        self.phone_number = phone_number
        self.address = address
        self.score = score


student1 = Student('박지민', 3, 2, '010-1111-2222', '부산시 동래구', 90)
student2 = Student('이준국', 3, 2, '010-1111-2222', '부산시 동래구', 90)
student3 = Student('이도경', 3, 2, '010-1111-2222', '부산시 동래구', 90)
student4 = Student('이주헌', 3, 2, '010-1111-2222', '부산시 동래구', 90)

print(student1)
print(student2)
print(student3)
print(student4)
