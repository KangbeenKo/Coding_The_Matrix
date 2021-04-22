# Pseudo Rndom Number Generation
## Linear Congruence Generator (LCG)

### x_(n+1) = (a*x_n + c) mod m, with seed x_0
### 2 <= a < m, 0 <= c < m


def lcg():
    ranNum = int(input('Choose your seed number(x_0): '))
    m = int(input('Select divisor(m): '))
    a = 1
    while a < 2 or a >= m:
        a = int(input('Enter the number for production(a): '))
        if a < 2 or a >= m:
            print("Error: the number 'a' must be 2 <= a < m. Please try again.")
    c = -1
    while c < 0 or c >= m:
        c = int(input('Enter the number for addition(c): '))
        if c < 0 or c >= m:
            print("Error: the number 'c' must be 0 <= c < m. Please try again.")
    
    numSet = set()
    
    for i in range(100):
        ranNum = (a*ranNum + c) % m
        numSet.add(ranNum)
    numSet = sorted(list(numSet))
    print(numSet)

lcg()
