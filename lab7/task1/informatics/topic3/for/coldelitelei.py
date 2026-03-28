x = int(input())
counter = 0
for i in range(1, int(x**0.5)+1):
    if x % i == 0:
        if i * i == x:
            counter += 1
        else:
            counter += 2
print(counter)