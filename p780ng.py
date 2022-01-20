from email.policy import default
from math import *
from collections import *
from cyclehelper import *
from lev import *

D = defaultdict(int)
LIMIT = 10**5
for m in range(1, LIMIT+1):
    for k in range(m+1, LIMIT+1):
        if m==0: continue
        NMIN = int(sqrt(12*k**2*m**2))+1
        if NMIN>LIMIT: break        
        print(f"NMIN={NMIN:5}")
        C = getcycle(k,m)
        for n in range(NMIN, LIMIT+1):
            if (C*n) % (2*k) == 0 :
                #print(f"n={n} k={k} m={m} C = {C} D[n]={D[n]} B={C*n/2/k}")                
                D[n] += 8

S = 0
for n in range(LIMIT+1):
    S += D[n] + parallel(n)
    print(f"n={n:5} N={D[n]:5} parallel={parallel(n):5} S={S:5}")            
