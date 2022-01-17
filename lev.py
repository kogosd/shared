from math import *

def parallel1(N):
    # rectangle parallel to sides, m * y = N * 3 / 4
    n_sol = 0
    if N % 2 == 0:
        y_times_m = N
        # one edge of triangles parallel to rectangle side
        # strip of triangle exists only with even number of triangles
        # loop will be slow for large numbers
        # but I do not see how to reduce as divisors are needed
        n_s = int(sqrt(y_times_m)) + 1
        for j in range(1, n_s):
            if j != 1 and y_times_m // j * j != y_times_m:
                continue
            if y_times_m // j % 2 == 0 and j % 2 == 0: # and j * j != y_times_m:
                n_sol += 2
            elif y_times_m // j % 2 == 0 or j % 2 == 0:
                n_sol += 1

            n_sol += 2
            # if N == 14:
                # if j % 2 == 0:
                #    print(" a " + str(j//2) + " b " + str(N//j * sqrt(3)/2) + " area " + str(j * N//j * sqrt(3)/4))
                # if N//j % 2 == 0:
                #    print(" a " + str(j * sqrt(3)/2) + " b " + str(N//j / 2 ) + " area " + str(j * N // j * sqrt(3) / 4))
            """
            if y_times_m // j % 2 == 0:
                n_sol += 2
            if j % 2 == 0 and j != y_times_m // j:
                n_sol += 2
            """
    return n_sol

def parallel(N):
    n_par = 0
    if N % 2 == 0:
        y_times_m = N
        # one edge of triangles parallel to rectangle side
        # strip of triangle exists only with even number of triangles
        # loop will be slow for large numbers
        # but I do not see how to reduce as divisors are needed
        n_s = int(sqrt(y_times_m)) + 1
        for j in range(1, n_s):
            if j != 1 and y_times_m // j * j != y_times_m:
                continue
            if y_times_m // j % 2 == 0 and j % 2 == 0 and j * j != y_times_m:
                n_par += 4
            elif y_times_m // j % 2 == 0 or j % 2 == 0:
                n_par += 2
    return n_par

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

def solve_x(N, m, k):
    c = 27/64*k*m*k*m*m*m
    b = 9/8*k*k*m*m - 3/16*N*N # 3/4
    a = 3/4*k*k
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
        # print("x1 " + str(x1) + ' x2 ' + str(x2))
    return x1, x2

def solve_y(x, m, k):
    if x < 0:
        return None
    if x == 0:
        return 0 # solve me
    y =  3 * m * k / x /4
    # if int(2 * y) < 2 * y - 1e-8:
    #    return None

    return y



def F(N):
    sols = []
    n_sol = 0
    for m in range(1, N):
        for k in range(1, N): # int(N * 2/ sqrt(3)/m) + 1):

            def check_xy(x_d, y_d, k, m , N):
                    if fabs(x_d * y_d - 3 *k * m) > 1e-8:
                        return
                    if fabs((x_d  * x_d + m * m * 3 ) * (y_d * y_d + k * k * 3) - 3 * N * N) < 1e-8:
                        print(" N " + str(N) + ' x ' + str(x_d) + ' y ' + str(y_d) + ' k ' + str(k) + ' m ' + str(m))
            """
            for x_d in range(1, 2 * N + 1):
                for y_d in range(1, 2 * N + 1):
                    check_xy(x_d, y_d, k, m, N)
            """

            x1, x2 = solve_x(N, m, k)

            for x in [x1, x2]:
                if x1 is None:
                    continue
                # if int(2*x) < 2*x - 1e-8 or fabs(x - 0.5 * m) <1e-8:
                if fabs(x - 0.5 * m) <1e-8:
                    continue
                y = solve_y(x, m, k)
                if y is None or y == 0:
                    continue
                # check_xy(x * 2, y * 2, k, m, N)
                #if int(2*y) < 2 * y - 1e-8 or fabs(y - 0.5 * k) <1e-8:
                if fabs(y - 0.5 * k) <1e-8:
                    continue


                def travel_check(x, y, k, m):
                    if m == k:
                        return not int (x + y + 0.5 * 1.e-8) < x + y - 1e-08
                    if m < k:
                        hor_line = x + m * y / k
                        dist_d = {}
                        for ll in range(m + k -1, 0, -1):
                            cnt = 1
                            l = ll
                            while l != 0 and l not in dist_d:
                                dist_d[l] = hor_line * cnt
                                cnt += 1
                                l += m
                                if l >= k:
                                    l = l - k
                            dist_val = hor_line * (cnt - 1) - (dist_d[l] if l > 0 else 0)
                            if int(dist_val + 0.5 * 1.e-8) < dist_val - 1e-08:
                                return False
                        return True
                    else:
                        hor_line = y + k * x / m
                        dist_d = {}
                        for ll in range(m - 1, 0, -1):
                            cnt = 1
                            l = ll
                            while l != 0 and l not in dist_d:
                                dist_d[l] = hor_line * cnt
                                cnt += 1
                                l += k
                                if l >= m:
                                    l = l - m

                            dist_val = hor_line * (cnt - 1)- (dist_d[l] if l > 0 else 0)
                            if int(dist_val + 0.5 * 1.e-8) < dist_val - 1e-08:
                                return False
                        return True


                #val = x * k + m * y # x * k / m + y
                #if int(val + 1/2*1.e-8) < val - 1e-08:
                #    continue
                # val = y + x * k / m
                # if int(val + 1 / 2 * 1.e-8) < val - 1e-08:
                #    continue
                # else:
                #    if int(0.5 + x + y + 1.0e-8) < 0.5 + x + y + 1.0e-8:
                #        continue
                if not travel_check(x, y, k, m):
                    continue
                sols.append((x, m, y, k))
                if N == 14:
                    a = sqrt(x*x + 3/4*m*m)
                    b = sqrt(y*y+3/4*k*k)
                    # print(" a " + str(a) + " b " + str(b) + " a*b " + str(a*b))
                same_sides = 1 if fabs((x*x + m*m*3/4) - (y*y + k*k*3/4) ) < 1e-8 else 2
                if m != k:
                    n_sol += 2 * same_sides
                else:
                    n_sol += 1 * same_sides

    n_sol += parallel(N)
    return n_sol
