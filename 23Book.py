#23Book.py

import json
books = list()
books.append( {"제목":"파이썬 정보", "출판년도":"2022", "출판사":"국민은행", "페이지":123, "가격":10000, "재고":True })
books.append( {"제목":"자바 정보", "출판년도":"2012", "출판사":"우리출판", "페이지":12323, "가격":11000, "재고":True })
books.append( {"제목":"C 언어 정보", "출판년도":"2021", "출판사":"국민은행", "페이지":1423, "가격":16000, "재고":False })
books.append( {"제목":"파이참 정보", "출판년도":"2011", "출판사":"삼성출판", "페이지":723, "가격":8000, "재고":True })
books.append( {"제목":"구글 정보", "출판년도":"2014", "출판사":"국민은행", "페이지":723, "가격":6000, "재고":True })

for book in books:
    print(book)

import json

#with open("./book.json", "w", encoding="utf8") as f:
#    json.dump(books, f)

with open("./book.json", "r", encoding="utf8") as f:
    readBooks = json.load(f)

print("====================")
for book in readBooks:
    print(book)
    print(book["제목"])

