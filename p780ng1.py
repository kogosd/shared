from math import *
from collections import *
import sys

D = defaultdict(int)
MOD=10**9+7
LIMIT = int(sys.argv[1])
sqrt12 = sqrt(12)
sqrt3 =  sqrt(3)
S = 0


def getcycle(k,n):
    return max(k,n)//gcd(k,n)

def process_n(k, NMIN, C, LIMIT, D, increment):
    global S
    n = 0
    for n in range(NMIN, LIMIT+1):
        if C*n%(2*k) == 0: break
    if n==0: return
    S+= increment* (C*(LIMIT+1) - C*n)//(2*k) + 1

#k>m
for m in range(1, LIMIT+1):
    print(f"1. m={m:6}")  
    if m*(m+1)*sqrt12 > LIMIT: break  
    for k in range(m+1, LIMIT+1):
        if k%1000000==0: print(f"1.    k={k:6}")          
        NMIN = int(floor(m*k*sqrt12))+1
        if NMIN>LIMIT: break      
        C = getcycle(k,m)
        process_n(k, NMIN, C, LIMIT, D, 8 )
#k==m
for m in range(1, LIMIT+1):
    print(f"2. m={m:6}")    
    NMIN = int(m*m*sqrt12) + 1
    if NMIN>LIMIT: break        
    process_n(m, NMIN, 1, LIMIT, D, 2 )

#k==0
for m in range(1, LIMIT+1):
    if m%1000000==0: print(f"3. m={m:6}")    
    NMIN = 2*m
    if NMIN>LIMIT: break  
    process_n(m, NMIN, 1, LIMIT, D, 2)      

print(f"S={S} SMOD={S%MOD}")
