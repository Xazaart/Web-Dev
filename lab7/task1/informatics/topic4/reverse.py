n = int(input())
a = input().split()
i = 0

while(n > i):
    a[i], a[n-1] = a[n-1], a[i]
    i += 1
    n -= 1

for i in a:
    print(i, end=" ")