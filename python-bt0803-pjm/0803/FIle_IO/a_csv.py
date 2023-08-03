### CSV 파일 입출력 ###

# CSV 파일
# :  Comma Separated Values (쉼표로 분리된 값)
# : 필드(데이터)를 쉼표로 구분한 파일
# : 표 형태의 데이터를 저장할 때 사용
# 열: 쉼표로 구분
# 행: 새 줄로 구분

# 이름, 학년, 반
# 박지만, 1학년, 6반
# 이준국, 2학년, 8반

# 1. CSV 파일 읽기
# - 한 줄에 한 데이터: readline() 메소드로 한 줄씩 읽기
# - 쉼표로 분리: split() 메소드

import csv
student_list = []
with open('C:\\python-bt0720\\python-bt0803-pjm\\0803\\FIle_IO\\student.csv', 'rt', encoding='utf-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(', ')
        student_list.append(student)
print(student_list)

# 2. CSV 모듈 사용
# csv 모듈로 csv 파일 읽기
# : csv.reader() 메소드는 csv 파일의 내용을 읽고
# : 그 내용을 저장한 객체를 반환

with open('C:\\python-bt0720\\python-bt0803-pjm\\0803\\FIle_IO\\student.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# csv 모듈로 csv 파일 생성
# csv.writer 객체를 이용하여 csv 파일 작성 가능

header = ['이름', '나이', '직업']
data = [['박지민', 50, 'Developer'], ['이준국', 50, 'Doctor']]

with open('person.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
