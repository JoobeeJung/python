#39dbSelect.py
from pymongo import MongoClient
import time
import os

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test']
    print('저자\t\t', '제목\t', '종류')
    for d in db['posts'].find():
         print(d['author'], '\t', d['title'], '\t', d['kind'])

    print('전체레코드갯수 =', db['posts'].estimated_document_count())
    print('=' * 100)
    print()

    name = input('저자검색입력 >>> ')
    search = db['posts'].find_one( { 'author': name} )
    if search is None:
        print(name, ' 검색결과가 없습니다')
        exit(-1)

    print(search ['author'], search ['title'], search ['kind'])

    # print()
    # time.sleep(2)
    # name2 = input('저자검색입력 like >>> ') #~~T where author like '%t%' ;
    # search2 = db['posts'].find({'author': { '$regex':name2} })
    # for d2 in search2:
    #     print(d2['author'], d2['title'], d2['kind'])
    # # print('조회레코드갯수 =', db['posts'].estimated_document_count())
except Exception as err:
    print('db조회에러발생 : ', err)

