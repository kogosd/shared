from email.policy import default
from math import *
from collections import *
from cyclehelper import *
from lev import *
import sys
from p780 import *

D = defaultdict(int)
MOD=10**9+7
LIMIT = int(sys.argv[1])
sqrt12 = sqrt(12)
sqrt3 =  sqrt(3)
EPSILON = 1e-6
for m in range(1, LIMIT+1):
    for k in range(m, LIMIT+1):
        NMIN = int(m*k*sqrt12)
        if NMIN>LIMIT: break        
        print(f"m={m:6}  k={k:6}  NMIN={NMIN:5}")
        C = getcycle(k,m)
        for n in range(NMIN+1, LIMIT+1):
            if (C*n) % (2*k) == 0 :
                #print(f"n={n} k={k} m={m} C = {C} D[n]={D[n]} B={C*n/2/k}")                
                DD = n**2 - 12*k**2*m**2
                x1 = (n-sqrt(DD))/4/k
                x2 = (n+sqrt(DD))/4/k
                t1 = sqrt3/2/m/x1
                t2 = sqrt3/2/m/x2
                increment = 4 if m!=k else 1
                if abs(t1-1./sqrt(3.)) > EPSILON and abs(t1-sqrt(3.)) > EPSILON:                    D[n] += increment
                if abs(t2-1./sqrt(3.)) >EPSILON and abs(t2-sqrt(3.)) > EPSILON:                    D[n] += increment

S = 0
for n in range(LIMIT+1):
    S += D[n] + parallel(n)
    print(f"n={n:15} N={D[n]:15} parallel={parallel(n):15} S={S:15} SMOD={S%MOD}")            
