# 04Immutable.py
# Mutable (변할 수 있는), Immutable(변할수 없는)

# Mutable 예: int , str
a = "Hello"
print(id(a))
a = "World"
print(id(a))

myList = ["Hello", 123, [1, 2, 3, 4]]  #myList[2][1]
print(myList)
print(type(myList))
print(id(myList))

myList[0] = "안녕하세요"
print(myList)
print(type(myList))
print(id(myList))

myList = "World"
print(myList)
print(type(myList))
print(id(myList))

# 데이터 구조
# 1. List : [ ]
lotto = [11, 22, 33, 44, 55, 66]
print(lotto)
print("type of  lotto = ", type(lotto))
val0 = lotto[0];
print(val0)
val = lotto[-2]
print(val)

# list :  11 22 33 44 55 66
# index:  0  1  2  3  4  5
# n-idx : -6 -5 -4 -3 -2 -1
size = len(lotto)
print("size of lotto = ", size)
print(lotto[5])

lotto.append(77)
lotto.append(30)
print(lotto)

# remove(값)
lotto.remove(33)
print(lotto)
lotto.insert(1, 333)
print(lotto)

val = lotto.pop(4)  # list=> ls , remove => rm
print("val = ", val)
print(lotto)

small = lotto[1:6]
print(small)
print(lotto[1:4])

print(lotto)
clone = lotto
clone.append(999)
print(lotto)

print("id lotto = " , id(lotto))
print("id clone = ", id(clone))

copyList = lotto[:]
copyList.append(1111)
print("lotto  = ", lotto)
print("copyList = ", copyList)

# List 합치기..
a = [1,2,3]
b = [4,5,6]

c = a + b
print("c = ", c)

lang = ["Python", "C", "Java", "C++"]
print(lang)
lang.append(10)
lang.append(20)
print(lang)

# nested : 중첩, 내포 list
nest = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]

print(nest[1])
print(nest[-1])
print(nest)
print(nest[:])
print(nest[1][2])

pgm = "Python Programming"
print(pgm[0])
print(pgm[0:7])
print(pgm[-3:])

# 빈 list 만드는 법 2가지 : empty list
emptyList = []
print(type(emptyList))
print(id(emptyList))

empty = list()

# tuple : 쌍
# 5-tuple : srcIP, srcPort, dstIP, dstPort, protocol(TCP/UDP)

movie = "슈퍼맨", 1980, "배트맨", 1995, "오징어", 2021
print(movie)
print(movie[0])
print(movie[1])
size = len(movie)
print("size = ", size)
print(type(movie))

table = [1,2,3], [4,5,6]
print(table)
print(type(table))
print(type(table[0]))
print(type(table[0][1]))

# 6 -> 66
table[1][2] = 66
print(table)

# 빈 튜플 만들기
emptyTuple = ()
print(type(emptyTuple))

myString = "Hello"
myTuple = "Hello",
print(type(myString))
print(type(myTuple))

print(movie)
a, b, c, d, e, f = movie
print("c = ", c)

## tuple --> list
movieList = list(movie)
print(movieList)

# Set
#  10 30 20 40 22
# A = { 1, 2, 1, 3, 1, 4, 2, 3, 2, 2 } = {1, 2, 3, 4 }

lang = {"C", "C++", "Java", "C", "Python", "Java", "C++", "PHP", "C"}
print(lang)

a = set("samsungmulticampus")
b = set("kbstarmoonjaewoo")
print(a)
print(b)
print(a-b)
# && , and  = > a & b  : Intersection
# ||  or    = > a | b  : Union
print(a & b)
print(a | b)
print(a ^ b)

# Dictionary Type
# key:value
# dict[apple] , 사과

colors = {"RED":1, "BLUE":2, "YELLOW":3 }
print(colors)
dict = {"apple":"사과", "desk":"책상", "note":"공책"}
print(dict)
print(dict["apple"])
# 연관배열, associative array
#print(dict["phone"])
dict["phone"] = "전화기"
print(dict)
dict["book"] = "책"
print(list(dict.keys()))
print(sorted(dict.keys()))
print(sorted(dict.keys(), reverse=True))

print(sorted(dict.values()))

