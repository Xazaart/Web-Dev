from math import ceil

shoklniki = int(input("Enter shoklniki number: "))
yabloki = int(input("Enter yabloki number: "))

print(int((yabloki-yabloki%shoklniki)/shoklniki))
print(ceil((yabloki-yabloki%shoklniki)/shoklniki))