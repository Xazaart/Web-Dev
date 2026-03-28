n = int(input())
nums = []

a = input().split()

counter = 0

for i in range(1,n):
    if(int(a[i-1]) < int(a[i])):
        counter += 1
print(counter)