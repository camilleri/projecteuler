# Stategy: 1 + 2 + ... + n = n ( n + 1 ) / 2
#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())-1

    # sum multiples of 5
    x5 = n//5
    res = 5*(x5*(x5+1)//2)
    
    # sum multiples of 3
    x3 = n//3
    res += 3*(x3*(x3+1)//2)

    # multiples of 15 would have been counted twice
    x15 = n//15
    res -= 15*(x15*(x15+1)//2)    
            
    print(res)