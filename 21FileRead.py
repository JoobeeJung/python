# 21FileRead.py

file = open("./test.txt", "a", encoding="utf8")
file.write("Hello File Write Test\n")

name = input("Insert name : ")
file.write("안녕하세요... " + name + "님 반갑습니다.\n")

for x in range(10000000):
    file.write(str(x +1) + "\n")

file.close()

readFile = open("./test.txt", "rt", encoding="utf8")
for line in readFile:
    print(line)

readFile.close()