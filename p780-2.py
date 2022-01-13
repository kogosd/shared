from math import *
sqrt3= sqrt(3.)
def solveq(a, b, c):
    if a == 0:
        if b == 0:
            return None, None
        else:
            return -c/b, None
    D = b*b-4*a*c
    if D<0: return None, None
    d = sqrt(D)
    x1 = (-b + d)/2/a
    x2 = (-b-d)/2/a
    return x1, x2

def solve_x(N, k, n):
    c = 27* k**4 * n**2
    b = 72* k**2*n**2 - 12*N**2
    a = 48*n**2
    x1, x2 = solveq(a, b, c)
    if x1 is not None:
        if x1 < 0:
            x1 = None
        else:
            x1 = sqrt(x1)
    if x2 is not None:
        if x2 < 0:
            x2 = None
        else:
            x2 = sqrt(x2)
        #print("x1 " + str(x1) + ' x2 ' + str(x2))
    return x1, x2

def solve_y(x, k,n):
    if x < 0:
        return None
    if x == 0:
        return 0 # solve me
    val =  3. * n * k
    y = val/4/x
    #if y * 4 * x != val:        return None

    return -y


def L(x,y):
    return sqrt(x*x +y*y)

def F(N):
    sols = set()
    S=0
    for k in range(-N, N):
        if k==0: continue
        for n in range(1, N):
            if abs(k)*n > N/2/sqrt3: break
            x1, x2 = solve_x(N, k, n)

            for x in [x1, x2]:
                if x is None:   continue
                #if int(2*x) < 2*x - 1e-8:                    continue
                y = solve_y(x, k,n)
                if y is None or y == 0:                    continue
                #if int(2*y) < 2 * y - 1e-8:                    continue

                if False:
                    A=L(x, sqrt3*k/2)
                    if A==0: continue
                    B=L(y, sqrt3*n/2)
                    if B==0: continue

                    
                    #print("A={}, B={} k ={} n={} x={} y={} x*y*4/3/k/n={} ".format(A,B,k,n,x,y,x*y*4/3/k/n))
                #sols.add((x,y))
                S+=1

    #return S

    # rectangle parallel to sides, n * y = N * 3 / 4
    n_sol = S #len(sols)
    if N % 2 == 0 and N // 3 * 3 == N:
        y_times_m = N // 3 * 4
        # one edge of triangles parallel to rectangle side
        # strip of triangle exists only with even number of triangles
        # loop will be slow for large numbers
        # but I do not see how to reduce as divisors are needed
        n_s = int(sqrt(y_times_m)) + 1
        for j in range(1, n_s):
            if j != 1 and y_times_m // j * j != y_times_m:
                continue
            if y_times_m // j % 2 == 0:
                n_sol += 2
            if j % 2 == 0 and j != y_times_m // j:
                y_times_m += 2
    return n_sol

S = 0
for N in range(1, 10**5+1):
    n_sol = F(N)
    S += n_sol
    print("f is {} for {}, G={}".format(n_sol,N,S))
