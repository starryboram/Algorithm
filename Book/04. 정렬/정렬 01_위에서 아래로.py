n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for i in sorted(array):
    print(i, end = '')
    