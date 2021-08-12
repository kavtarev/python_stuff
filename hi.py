b = list(map(int, input().split()))
tmp = 0
for i in b:
    tmp += b.count(i) - 1
print(tmp//2)

