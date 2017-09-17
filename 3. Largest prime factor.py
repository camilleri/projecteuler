#!/bin/python

import sys
import math

n = 0
i = 0

def loop():
    global n
    global i
    i = 3
    while i <= math.sqrt(math.floor(n)):
        if(n%i == 0):
            n = n/i
            return True
        i += 2
    return False
        

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    
    while (n%2 == 0):
        n = n / 2
    
    if (n == 1):
        print(2)
    else:
        execute_loop = True
        while(execute_loop):
            execute_loop = loop()
        if (n > 2):
            print(n)
        else:
            print(i)