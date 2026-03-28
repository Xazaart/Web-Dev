n = int(input())
if(n == 1):
    print("YES")
elif(n % 2 != 0):
    print("NO")
else:
    while(True):
        if(int(n) != n):
            print("NO")
            break
        elif(n == 1):
            print("YES")
            break
        n /= 2
