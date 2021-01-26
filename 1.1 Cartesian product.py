A = {1,2,3}
B = {'♡', '♠', '♣', '◇'}

answer = set()

def cartesian(a,b):
    for i in a:
        for j in b:
            answer.add((i,j))
    return answer

print(cartesian(A,B))