a,b,c = map(int,input().split())
if a > b:
    if a > c:
        g = a
    else:
        g = c
else:
    if b > c:
        g = b
    else:
        g = c
print(g)