# input val. is from Domain.
# input = pre-image / output = image

''''''
# Example 1.3.1: Doubling Function
D = {1,2,3,4,5,6,7,8}
answer = set()
def doubFunc(domain):
    for i in range(len(domain)):
        answer.add((i+1,(i+1)*2))
    
    return answer

print(doubFunc(D)) # There is no order in the set

''''''
# Example 1.3.2: Multiplication Function
D = {1,2,3,4,5,6,7,8}
answer = set()
def multFunc(domain):
    for i in range(len(domain)):
        for j in range(len(domain)):
            answer.add(((i+1, j+1),(i+1)*(j+1)))
    
    return answer

print(multFunc(D))

''''''
# for function f, the image of input q for f is represented as f(q)
# if r = f(q), we say 'q is mapped by f to r' => f : q->r
# co-domain is a set of function values selected
# function f : domain D -> co-domain F

''''''
# Example 1.3.3: Caesar cryptosystem

# A->D, B->E, ... , Y->B, Z->C (wrap-around)
# plaintext to ciphertext

# D = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'} 
# ASCII code can be used for domain (co-domain is same with domain, in this example)
# ord('A'), ord('X'), ord('Z') -> 65 88 90

def caeser():
    plaintext = input("Enter the text: ").upper()
    ciphertext = ""
    txt = []
    for i in range(len(plaintext)):
        txt.append(ord(plaintext[i]))   # ord(char): ASCII of Python
        if txt[i] < 88:
            txt[i] += 3
        else:
            txt[i] = txt[i]%88 + 65
    
        ciphertext += chr(txt[i])   # ord(char) = char to int / chr(int) = int to char 

    return f"{plaintext} -> {ciphertext}"

print(caeser())

''''''
# Example 1.3.4: cosine
# range is a set of function values for all domain elements
# cos: R -> R (range: only -1 ~ 1)

''''''
# Example 1.3.5: product function

# input: set of integer which is bigger than 1 -> domain
# set of all integer which is bigger than 1 -> co-domain
# range: composite number(prime numbers are excluded)

answer = set()
def prodFunc():
    d1, d2 = map(int, input().split())
    answer.add(f"d1 * d2 = {d1*d2}")

    return answer

print(prodFunc())

''''''
# A procedure is an accurate description of the computational problem's computing step
# input(parameter) -> outpur(return value)

''''''
# Example 1.3.6: procedure in Python

def mul(p,q) : return p*q

''''''
# computational problems are input-output specification that maybe needs the procedure

# Example 1.3.7 - same with 1.3.6

# Example 1.3.8
# input: integer 'm' which is bigger than 1
# output: the set of integer which the product of elements is m

answer = set()
def findRoot():
    m = int(input())
    for i in range(1,m+1):
        if m%i == 0:
            answer.add((i,m//i))
    
    return answer

print(findRoot())

''''''
