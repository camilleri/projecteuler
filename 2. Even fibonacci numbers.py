# Strategy DP fibonacci
#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prev1 = 1
    prev2 = 2
    res = 2
    fib = prev1 + prev2
    while(fib < n):
        if (fib%2==0):
            res += fib            
        prev1 = prev2
        prev2 = fib
        fib = prev1 + prev2
        
    print(res)