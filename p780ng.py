from email.policy import default
from math import *
from collections import *
from cyclehelper import *
from lev import *

D = defaultdict(int)
for k in range(1, 200):
    for m in range(k+1, 200):
        NMIN = int(sqrt(12*k**2*m**2))+1
        if NMIN>100: continue        
        print(f"NMIN={NMIN:5}")

        C = getcycle(k,m)
        for n in range(NMIN, 200):
            print(f"n={n} k={k} m={m} C = {C} D[n]={D[n]}")
            if C*n % (2*k) == 0 :
                print(f"B={C*n//2//k}")
                D[n] += 4

S = 0
for n in range(101):
    S += D[n] + parallel(n)
    print(f"parallel of {n} is {parallel(n)}")
    print(f"n={n} N={D[n]} S={S}")            
