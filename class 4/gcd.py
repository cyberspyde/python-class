def gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if (m%i) == 0:
            fm.append(i)
        fn = []
    
    for i in range(1, n+1):
        if (n%i) == 0:
            fn.append(i)
        cf = []
    
    for f in fm:
        if f in fn:
            cf.append(f)
        
    return(cf[-1])

#print(gcd(837, 775))
#print(gcd(14, 63))

#  Compute gcd(14, 63)
# – Factors of 14 are [1, 2, 7, 14]
# – Factors of 63 are [1, 3, 7, 9, 21, 63]
# – Find largest element common to both lists
# ∗ For each factor of 14, check if it is also in the list of factors 63
# · Check 1 (yes), 2 (no), 7 (yes), 14 (no)
# – Common factors are [1, 7]
# – Largest of these is 7, so gcd(14, 63) = 7

def gcd2(m, n):
    fn = []
    fm = []
    for i in range(1, min(m,n) + 1):
        if (m%i) == 0:
            fm.append(i)
        if (n%i) == 0:
            fn.append(i)
        
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[-1])

#print(gcd2(14, 63))
#print(gcd2(837, 775))


def gcd3(m, n):
    cf = []
    for i in range(1, min(m, n) + 1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return(cf[-1])
    

# print(gcd3(14, 63))
# print(gcd3(837, 775))

def gcd4(m, n):
    if m == n:
        return m
    if m > n:
        return (gcd4(m-n, n))
    if m < n:
        return (gcd4(n-m, m))