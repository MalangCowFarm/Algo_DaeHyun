import math

A,B,V = map(int,input().split())

t = (math.ceil((V-A)/(A-B)))

print(t)


