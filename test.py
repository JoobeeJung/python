num = int(input("insert : "))
sum = 0

if num in range(1,101):
    for x in range(1, num+1):
        if(x % 2 ==0 or x % 3 ==0):
            print(x)
            sum += x
    print("sum : ", sum)

else:
    print("1부터 100 사이의 정수를 입력하세요.")