from functools import lru_cache
from math import *
from icecream import ic
from myturtle import *
from lev import *
import primefac as pf
import sys
from cyclehelper import *


def validate(k,n, N):
    a = 16*k**2
    b = -4*N**2
    c = 3*n**2*N**2
    x1,x2 = solveq(a,b,c)
    a1,a2=sqrt(x1), sqrt(x2)
    b1,b2 = N*sqrt(3)/4/a1, N*sqrt(3)/4/a2
    cos1, cos2 = 2*b1*n/N, 2*b2*n/N

    assert(abs(cos1)<=1)
    assert(abs(cos2)<=1)
    print(f"k={k:5} n={n:5} a1={a1:.3f},b1={b1:.3f},cos1={cos1:.3f},N1={a1*b1*4/sqrt(3)}   a2={a2:.3f},b2={b2:.3f},cos2={cos2:.3f},N2={a2*b2*4/sqrt(3)}")
    if not isclosetoany(abs(cos1), 0.5,sqrt(3)/2,0,1):
        clear()
        draw_title(str(N))
        draw_rectangle(0,0, 0,-b1, -a1, -b1, -a1, 0)
        draw_triangles_along_line(-a1/n,0, 0, -b1/k, N)
        draw_triangles_along_line(-2*a1/n,0, 0, -2*b1/k, N)  
        draw_triangles_along_line(-3*a1/n,0, 0, -3*b1/k, N)          
        wait ()
    if not isclosetoany(abs(cos2), 0.5,sqrt(3)/2,0,1):
        clear()
        draw_title(str(N))        
        draw_rectangle(0,0, 0,-b2, -a2, -b2, -a2, 0)
        draw_triangles_along_line(-a2/n,0, 0, -b2/k, N)
        draw_triangles_along_line(-2*a2/n,0, 0, -2*b2/k, N)  
        draw_triangles_along_line(-3*a1/n,0, 0, -3*b1/k, N)            
        wait()

    sin1 = sqrt(1-cos1**2)
    sin2 = sqrt(1-cos2**2)
    #assert(b1*sin1 == k*sqrt(3)/2)
    #assert(b2*sin2 == k*sqrt(3)/2)
    return cos1, cos2, sin1, sin2,  b1, b2


def isclose(x,y):
    return fabs(x-y) < 1e-8

def isclosetoany(x,*y):
    for elm in y:
        if isclose(x,elm): return True
    return False

def isint(x):
    return isclose(x, int(x))

@lru_cache()
def alt(N):
    count = 0
    for k in range(1, N):
        if k==0: continue
        for n in range(1, N):
            #if n==k: continue #parallel??
            if abs(k*n) > N/2/sqrt(3): break
            cos1,cos2 ,sin1,sin2, b1, b2=  validate(k,n, N)
            #f travel_check(b1/cos1, n, k)==True: count += 1
            #if travel_check(b2/cos2, n, k)==True: count += 1
            #continue
            C = getcycle(k,n)
            print(f"cycle for k={k} n={n} is {C}")

            if not isclosetoany(abs(cos1), 0.5,sqrt(3)/2,0,1) : 
                if isclose(b1*sin1, k*sqrt(3)/2): 
                    if isint(C*b1/cos1): count += 1
            if not isclosetoany(abs(cos2), 0.5,sqrt(3)/2,0,1) : 
                if isclose(b2*sin2, k*sqrt(3)/2): 
                    if isint(C*b2/cos2): count += 1

            #find cycle length
            
            #ic (N,k,n)

    return count*2

@lru_cache()
def alt2(N):
    M = pf.factorint(N)
    P=1
    for k,v in M.items():
        P*=(v+1)
    return P*16


G = 0
G_ALT = 0
NMIN=1
NMAX=int(sys.argv[1])
TURTLE=False
for N in range(NMIN, NMAX+1):
    n_sol = F(N)
    G_ALT += alt(N) + parallel(N)
    G += n_sol    
    print("f for {:5} is {:5}, parallel={:5} alt={:5} G_ALT={:5} G={:5}".format(N, n_sol, parallel(N), alt(N)+parallel(N), G_ALT, G))
print("f for {:5} is {:5}, parallel={:5} alt={:5} G_ALT={:5} G={:5}".format(N, n_sol, parallel(N), alt(N)+parallel(N), G_ALT, G))

wait()