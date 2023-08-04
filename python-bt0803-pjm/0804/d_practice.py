# 교재 p.270 예제

class Book:
    # 인스턴스 변수
    title = ""
    author = ""

    # 인스턴스 메서드
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'Title : {self.title}, Author : {self.author}')
    
book1 = Book()
book2 = Book()

book1.set_info('파이썬', '박지민')
book2.set_info('어린왕자', '생택쥐페리')

book_list = [book1, book2]

# 각 인스턴스의 정보 출력
for book in book_list:
    book.print_info()