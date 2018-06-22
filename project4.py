# projecteuler.net problem ID 4, largest palindrome product, find the largest palindrome made from the prodcut of 2 three digit numbers


def isPalindrome(p):
    pStr = str(p)
    for x in range(p):
        pRev[x] = pStr[(p-x)-1]
        print(pRev)

isPalindrome(5)
