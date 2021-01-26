# Example 1.2.1
A = {1,2,3}
B = {'♡', '♠', '♣', '◇'}

answer = set()

def cartesian(a,b):
    for i in a:
        for j in b:
            answer.add((i,j))
    return answer

CartesianProduct = cartesian(A,B)

print(CartesianProduct)

''''''

# Quiz 1.2.2
print(len(CartesianProduct))

''''''

# Proposition 1.2.3: 유한 집합 A와 B에 대해, |A X B| = |A| * |B| 이다.

''''''

# Quiz 1.2.4
Q = {1,2,3,4,5,6,7,8,9,10,'J','Q','K'}
print(len(cartesian(Q,B)))