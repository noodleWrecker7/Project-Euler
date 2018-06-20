# projecteuler.net problem ID 3, largest prime factor, find the largest prime factor of 600851475143

n = 600851475143
hpf = 0

def isPrime(i):
    for t in range(i):
        if t == 0:
            t += 1
        if i % t == 0:
            return False
        else:
            return True


for x in range(n):
    if x % 10000000 == 0:
        print(x)
        print((x / n) *100)
    if x == 0:
        x += 1
    if (n % x) == 0:
        if isPrime(x):
            hpf = x

print(hpf)
