#05If.py
# 제어문.. : switch 가 없다.
# if, while, for, continue, pass
# if ~elif

color = input("red or blue : ")
print(color)

if color == "red":
    print("Stop")
elif color == "blue":
    print("Pass")
else:
    print("Unknown")

# 신호등의 색을 받는다.
# 빨간색이면 멈추세요.
# 파란색이면,
#       준비되었나요(yes/no)
#       yes : 건너세요.
#       no : 다음에 건너세요.
# 빨/파랑이 아니면 알 수 없는 색입니다.

# while:

counter = 0
color = ""
stopFlag = False

while stopFlag == False:
    color = input("red / blue : ")
    if color == "red":
        counter = counter + 1
        print("Stop ")
    elif color == "blue":
        answer = input("yes / no : ")
        if answer == "yes":
            print("Pass !!")
            stopFlag = True
        else:
            counter = counter + 1
            print("Wait !!")
    else:
        counter = counter + 1
        print("Unknown Color")
print("Counter = " , counter)
