# 08Pass.py

for x in range(1,11):
    if x % 2 == 0:
        pass
    else:
        print("odd")
    print("-")

squares = []
for x in range(10):
    squares.append(x**2)

for x in squares:
    print(x)

squares = [ x**2 for x in range(10)]

pairs = []
A = ["aaa", "bbb", "ccc"]
B = ["ccc", "ddd", "aaa"]
# a list 순회
#   b list 순회
#       ax !=by 일 때 pairs.append( (ax, by) )

for a in A:
    print(a)
    for b in B:
        print(b)
        if a != b :
            pairs.append((a, b))
print(pairs)
