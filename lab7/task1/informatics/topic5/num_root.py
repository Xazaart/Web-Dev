def root(a, n):
    return a**n

nums = input().split()
a = float(nums[0])
n = int(nums[1])
print(root(a, n))