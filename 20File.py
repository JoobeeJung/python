# 20File.py

file = open("d:/fwrite.txt", "a", encoding="utf8")
file.write("Hello 111 국민은행 ★ ❤❤💖 漢字 123\n")

name = input("Insert Name : ")
message = "안녕하세요 " + name + "님 반갑습니다.\n"
result = file.write(message)
print("result = ", result)
# file.flush()
file.close()


print("*" * 80)

for x in range(1500):
    try:
        f = open("./xxx/" + str(x) + ".txt", "w")
    except IOError:
        print("Error : " , x)



"""
    for x in range(1000000):
        file = open("a.txt", "r")
        file.close()
        
"""