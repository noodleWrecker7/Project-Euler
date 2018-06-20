# projecteuler.net problem ID 1, 3 or 5, return the sum of all multiples of 3 or 5 below 1000

max = 1000
total = 0

for x in range(max):
    if(x % 3) == 0 or (x % 5) == 0:
        total += x
print(total)
