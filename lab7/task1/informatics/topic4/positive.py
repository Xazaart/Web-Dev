n = int(input())
nums = []

a = input().split()

counter = 0

for i in range(n):
    if(int(a[i]) > 0):
        counter += 1
print(counter)