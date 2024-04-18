#Program to Calculate Largest Among three Numbers
a,b,c = map(int,input("Enter the Three Numbers: ").split())

if a >= b:
    if a >= c:
        g = a
    else:
        g  = c
else:
    if b >= c:
        g = b
    else:
        g = c
print("Greatest Number is:", g)