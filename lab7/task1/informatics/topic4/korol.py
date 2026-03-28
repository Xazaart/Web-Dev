n = int(input())
a = input().split()

counter = 0

for i in range(1,n-1):
    if(int(a[i]) > int(a[i-1]) and int(a[i]) > int(a[i+1])):
        counter += 1

print(counter)