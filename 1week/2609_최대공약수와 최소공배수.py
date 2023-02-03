A,B = map(int,input().split())

def minium(A,B) :
    while B > 0 :
        A,B = B, A%B
    return A

def large(A,B) :
    return A*B // minium(A,B)

print(minium(A,B))
print(large(A,B))
