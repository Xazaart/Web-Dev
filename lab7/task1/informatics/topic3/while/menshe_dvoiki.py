n = int(input())
a = 0
while(True):
    if(2**a > n):
        break
    else:
        print(2**a)
    a += 1