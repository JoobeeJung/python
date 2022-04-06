#06For.py

# enhanced for
# for(int value : lotto)

colors = "red", "blue", "green", "yellow", "black"
size = len(colors)
print("size = ", size)
print("type color = ", type(colors))
for color in colors:
    print(color)

print("-" * 80)
# range(5) : 0, 1, 2, 3, 4
autoList = list(range(10))
print(autoList)

autoList = list(range(1, 5))
print(autoList)

autoList = list(range(1, 100, 3))
print(autoList)
sum = 0
for i in range(1, 11, 1):
    sum = sum + i

print(sum)

print("-" * 80)

# 사용자로부터 숫자를 입력받는다.
# 1부터 입력받은 수를 모두 출력하고, 합을 맨 마지막에 출력하시오.

# 1부터 입력받은 수까지의 2의 배수이거나 3의 배수를 모두 출력하시오.

number = int(input("Insert Number : "))


