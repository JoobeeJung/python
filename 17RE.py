# 17RE.py

import re

text = "My Id is nadopro and 123456-23-123456홍길동 password 010-1234-5a78is010-1234-5678이순신대한민국 !@#$%^&*123ABCDEFG123abcdef@@##$$"

# "A" 문자 찾기
print( re.findall("A", text) )
result = re.findall("A", text)
print("result = ", result)
print( re.findall("[ABC]{2}", text) )
print( re.findall("[가-힣]{3}", text))
print( re.findall("01[01]-[0-9]{4}-\d{4}", text) )
print( re.findall("[!@#$%^&*a-c]", text) )
print( re.findall("\D", text) ) # Not Decimal
print( re.findall("\d", text) ) # decimal
print( re.findall("[^a-z]", text) ) # not a-z
print("word : ",  re.findall("\w", text) ) # word
print( re.findall("\W", text) ) # Not Word
print( re.findall("\s", text) ) # space
print( re.findall("[0-9]{6}-\d{2}-\d{6}", text)) # 국민은행 통장
print( re.findall("[a-z][a-z]+", text))

myList = re.findall("[!@#$%^&*a-c]", text)
if len(myList) >=1 :
    print("Find !!!!")
else:
    print("Not Found !!!")


