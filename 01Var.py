
test = 13
print(test)
print("test = ", test)
print(type(test))
print(id(test))

test = 7;
print(test)
print("test = ", test)
print(type(test))
print(id(test))

test = "홍길동"
print(test)
print("test = ", test)
print(type(test))
print(id(test))

test = input("Insert Name ")
print(test)


# 변수 :  메모리가 매번 바뀐다.
# 데이터를 보고 타입이 자동으로 결정된다. int, str
# type 확인 : type(변수명)
# memory 확인 : id(변수명)

# name = 본인이름, age = 33
# 다음과 같이 출력하시오.
# 내 이름은 홍길동이고, 내년에는 34세입니다.
name = "홍길동"
age = 33
print("내 이름은 " , name , " 이고 내년에는 " , age +1 , "입니다.")


# 사용자 입력 받는 방법
# 변수명 = input("출력메시지")
myAge = input("Insert Age : ")
print("myAge = ", myAge)
print(type(myAge))

name = '작은 따옴표'
print(type(name))
print(name)
