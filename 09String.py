#09String.py

text = input("Insert Message in English : ")
print(text.upper(), end="")
print(text.lower(), end="\tAAA")
print(text.capitalize())

for c in text:
    print(c)

# 대문자로 입력된 것은 소문자로, 소문자-> 대문자로 출력하기
# Hello World
# hELLO wORLD

print("-" * 80)
for c in text:
    if c.isupper():
        print(c.lower() , end="")
    else:
        print(c.upper(), end="")

print("-" * 80)
rText = str()
for c in text:
    if c.isupper():
        rText += c.lower()
    else:
        rText += c.upper()
print("rText = ", rText)

test = "Hello World"
print(test.replace("Hello", "Oops"))
test = test.replace("Hello", "Oops2")
print(test)

print("text = " , text)
print("Swap = ", text.swapcase())

print("-" * 80)
# text를 역순으로 출력하시오.
# rText 에 역순을 저장한 후, rText를 출력하시오.
# range(10, -1, -1)
# range(1, 10, 1)

rText = str()
for c in range( len(text)-1, -1, -1 ):
    rText += text[c]
print("Reverse = ", rText)
print("Same = ", text[::-1])
