# Stategy: all palindromes of 6 digits are multiples of 11
#!/bin/python3

import sys
import bisect

# find palindromes
s = set()

def isPalindrome(num):
    if (num in s):
        return True
    
    if (num % 11 != 0):
        return False
    
    numStr =  str(num)
    if(len(numStr) != 6):
        return False
    for i in range(0,3):
        if (numStr[i] != numStr[5-i]):
            return False
    return True

for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        if (isPalindrome(i*j)):
            s.add(num)
            
s = sorted(s)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = bisect.bisect_left(s, n)
    print(s[i-1])