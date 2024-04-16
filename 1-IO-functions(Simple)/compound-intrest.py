P, R,T =map(int, input("Enter principal amount, time and rate of interest:").split())
CI = P * (pow((1 + R / 100), T))
print("Compound interest is", CI)
