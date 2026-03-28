def min4(a, b, c, d):
    return min(min(a,b), min(c, d))


nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])
print(min4(a, b, c, d))