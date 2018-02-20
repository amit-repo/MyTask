#!/usr/bin/python
"""
Generate random numbers in range (1,10) 100 times.

Desired output:
Number > 5 should have 73% of number generated
Number < 5 should have 27% of number generated
"""
import time
import itertools

# Api to generate random number based on epoch time
def generate():
    num = 10
    sec=time.time()
    for i in itertools.count():
        sec = sec % 100
        if(num >= sec):
            print(int(sec))
            break
        sec = sec % num

generate()



def seedLCG(initVal):
    global rand
    rand = initVal

#
# Api to generate random number using LCG(Linear Congruential Generator)
# Formula: Tx = ( a * Tx-1 + c) mod m
#
def lcg():
    a = 1140671485
    c = 128201163
    m = 2 ** 16
    global rand
    rand = (a*rand + c) % m
    return rand

seedLCG(100)

for i in range(20):
    print lcg()
