dva = input()
rev_dva = dva[::-1]
dec = 0
stepen = 0
for i in rev_dva:
    chislo = int(i)
    dec += chislo*2**stepen
    stepen += 1


print(dec)