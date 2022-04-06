#38dbInsert.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    print(client.list_database_names()) #admin,config,local
    print()

    db = client['test'] #데이터베이스생성
    print('test데이터베이스 생성 success 11:34 1:05')

    data_author = input('이름입력 >>> ')
    data_title = input('제목입력 >>> ')
    data_kind = input('종류입력 >>> ')

    data = {
        'author' : data_author ,
        'title' : data_title ,
        'kind' : data_kind
    }
    db.posts.insert_one(data) #insert into T명(필드1,필드2~~) values(데이터)
    print( data_author , '님 데이터 등록 성공했습니다 ')
    print('-' * 100)

    time.sleep(2)#2초후 데이터전체출력 for반복문  ['title']
    print('저자필드', '제목필드', '종류필드')
    print('=' * 50)
    for d in db['posts'].find(): #find()함수=select * from 테이블명
         #print(d)
         print(d['author'], d['title'], d['kind'])

    print('-' * 100)
except Exception as err:
    print('db에러발생 : ', err)