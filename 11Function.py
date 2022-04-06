# 11Function.py

def foo():
    name = input("Insert name : ")
    print(name , "님 반갑습니다.")

def bar():
    table = input(" 몇 단을 원하나? ")
    print(table , "단....")

# 인자 O, No Return
def sayHello(name):
    print("Hello Mr. ", name)
    print("Nice to Meet U")

def add(a, b):
    return a + b


#foo() # getYourName()
#bar()   # printMultiplication()
sayHello("Kim")
sayHello("Lee")

value = add(1,2)
print("value = ", value)

# 사용자로 부터 두 값을 입력받는다.
# 11 + 22 = 33

def noReturn(name):
    if name == "KIM":
        print("안녕하세요.")
        return
    else:
        print("Hello")

    print("Nice to see u.")
    return "OK"

ret = noReturn("KIM")
print(type(ret))

ret = noReturn("LEE")
print( type(ret) )

# range(10)
# range(0, 10)
# range(0, 10, 1)

def myRange(start, end=0, step=1):
    print("start = ", start , ", end = ", end , ", step = ", step)

myRange(10)
myRange(10, 5)
myRange(10, 5, 3)


# 가변 길이 인자
# * : tuple
# ** : Dict
def introFamily(name, *familyNames, **familyInfo):
    print("내 이름은 ", name, "입니다.")
    print("가족의 이름은 다음과 같다.")
    for name in familyNames:
        print(name)
    print("-" * 80)
    for key in familyInfo.keys():
        print(key, ":", familyInfo[key])

introFamily("홍길동", "엄마", "아빠", "형", "동생", "할머니", 주소="서울", 가훈="투표하자")
introFamily("이순신", "할머니", "할아버지" , 위치="선릉")

