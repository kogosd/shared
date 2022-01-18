
def getcycle(k,n):
    if k>n:
        k,n=n,k
    start = k
    end   = 0
    c = {}
    while len(c) < n:
        start = start%n
        c[start] = end
        start += 1
        end   += 1
    
    while len(c) > 0:
        curr_cycle = set()
        k = list(c.keys())[0]
        curr_cycle.add(k)
        while True:
            next = c[k]
            if next in curr_cycle:
                c.pop(k)
                return (len(curr_cycle))
                curr_cycle = set()
                break
            curr_cycle.add(next)
            c.pop(k)
            k=next


if __name__ == '__main__':
    for k in range(100):
        for n in range(k,100):
            print("=====>",k,n)
            print(getcycle(k,n))
