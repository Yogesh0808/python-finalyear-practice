n = 505
m = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig 
    n = n // 10
if rev == m:
    print("Palindrome")
else:
    print("Not a Palindrome")