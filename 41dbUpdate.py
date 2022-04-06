#39dbSelect.py
from pymongo import MongoClient
import time
import os

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    for d in db['posts'].find():
         print(d)

    name = input('검색입력 >>> ')

    search = db['posts'].find_one( { 'author': name} )
    print(search)
    if search is None:
        print(name, ' 검색결과가 없습니다')
        exit(-1)

    data_author = input('\n이름수정입력>>')
    data_title = input('제목수정입력>>>')
    data_kind = input('종류수정입력>>>')

    db['posts'].update_one(
        {'author':name},
        {
            "$set": {'author':data_author, 'title':data_title, 'kind':data_kind}
        }
    )
    print('수정 데이터 확인')
    for a in db['posts'].find():
        print(a)
except Exception as err:
    print('db조회에러발생 : ', err)

