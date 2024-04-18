n = int(input())
m = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n //= 10
if (m == rev):
    print("It is a Palindrome")
else:
    print("Not a Palindrome")