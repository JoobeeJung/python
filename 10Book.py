# 10Book.py

books = list()
# for book in books:
books.append({ "제목":"파이썬 정복", "출판일":"2022", "출판사":"국민출판사", "가격":5000, "재고유무":True })
books.append({ "제목":"자바 정복", "출판일":"2012", "출판사":"우리출판사", "가격":2000, "재고유무":False })
books.append({ "제목":"C언어 정복", "출판일":"2018", "출판사":"삼성출판사", "가격":15000, "재고유무":True })
books.append({ "제목":"컴퓨터 정복", "출판일":"2021", "출판사":"하나출판사", "가격":35000, "재고유무":False })
books.append({ "제목":"워드 정복", "출판일":"2015", "출판사":"컴정보", "가격":25000, "재고유무":True })
books.append({ "제목":"오피스 정복", "출판일":"2020", "출판사":"국민출판", "가격":3000, "재고유무":True })
books.append({ "제목":"파이썬 정복", "출판일":"2022", "출판사":"국민출판사", "가격":5000, "재고유무":True })
books.append({ "제목":"자바 정복", "출판일":"2012", "출판사":"우리출판사", "가격":2000, "재고유무":False })
books.append({ "제목":"C언어 정복", "출판일":"2018", "출판사":"삼성출판사", "가격":15000, "재고유무":True })
books.append({ "제목":"컴퓨터 정복", "출판일":"2021", "출판사":"하나출판사", "가격":35000, "재고유무":False })
books.append({ "제목":"워드 정복", "출판일":"2015", "출판사":"컴정보", "가격":25000, "재고유무":True })
books.append({ "제목":"오피스 정복", "출판일":"2020", "출판사":"국민출판", "가격":3000, "재고유무":True })


print(books)
#print(type(books))
#print(type(books[0]))

for book in books:
    print(book)

# 가격이 1만원 이상
highPrice = list()
existBook = list()
publishList = set()

for book in books:
    if book["가격"] > 10000:
        highPrice.append()
    publishList.add(book["출판사"])




