def xor(x, y):
    if((x == 1 and y == 1) or (x == 0 and y == 0)):
        return 0
    else:
        return 1

nums = input().split()
x = int(nums[0])
y = int(nums[1])

print(xor(x, y))