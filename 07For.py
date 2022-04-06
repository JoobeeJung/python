# 07For.py

# Java : Enhanced For
# for(int value :  lotto)
#    System.out.println(value)
# colors = "black",

colors = "aaa", "bbb", "ccc", "ddd", "eee", "fff"
print( type(colors))
for color in colors:
    print(color)

myList = list( range(10) )
print(myList)
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum = sum + x
        print("1 + 2 + 3 + ... + ", x )
    elif x % 3 ==0:
        print(x)
    else:
        print("xxx")
print("sum = ", sum)

# 사용자부터 입력(table) , 해당 단을 출력
# 3 * 1 = 3
# 3 * 2 = 6
# ...
# 3 * 9 = 27


print("-" * 80)

nest = [ [1,2,3], [4,5,6], [11, 22, 33]]
#        nest[0]  nest[1]   nest[2]
# for를 이용해서, 한줄에 하나씩 출력하시오.
# 출력 순서는 1,2,3,4,....33

for x in range(3):
    print(nest[x])
    for y in range(3):
        print(nest[x][y])

print("-" * 80)
nest = [ [1,2,3], [4,5], [11, 22, 33, 44], [1111, 2222, 3333, 4444, 5555], [77, 88]]
# for value in nest

for x in nest:
    print(x)
    for y in x:
        print(y)
# 예상 출력 결과
# 1
# 2
# 3
# 4
# 5
# ..
# 33



