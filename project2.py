# projecteuler.net problem ID 2, even fibonacci, find teh sum of all even fibonacci numbers below four million

max = 4000000

n1 = 1
n2 = 1
n3 = 0

total = 0

while (n1 + n2) < max:
    n3 = n1 + n2
    if (n3 % 2) == 0:
        total += n3
        print("n", n3)
    n1 = n2
    n2 = n3

print("total", total)
