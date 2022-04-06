#40dbDelete.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    name = input('삭제데이터 저자 >>> ')
    #search = db['posts'].find( { 'author': name} )
    #delete_one()사용해서 삭제처리후 전체출력
    search = db['posts'].delete_one({'author': name})

    if search is None:
        print(name, '검색결과가 없습니다.')
        exit(-1)
    for d in db['posts'].find():
        print(d)

except Exception as err:
    print('db삭제에러발생 : ', err)

