n = int(input())
nums = []

a = input().split()

for i in range(n):
    nums.append(int(a[i]))

for i in range(n):
    if i % 2 == 0:
        print(nums[i], end=' ')