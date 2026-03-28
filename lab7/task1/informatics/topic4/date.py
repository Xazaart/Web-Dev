n = int(input())
a = input().split()

counter = 0

for i in range(1,n):
    if(len(a[i]) == len(a[i-1])):
        counter += 1
        break
if(counter == 0):
    print("NO")
else:
    print("YES")