import random

print(random.getstate())

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Random integer:", random.randint(a, b))
#Prints a Random Integer within a Range
seq = input("Enter the sequence: ")
print("Random element from sequence:", random.choice(seq))

my_list = [20, 16, 10, 5]
random.shuffle(my_list)
print("Reshuffled list:", my_list)

print("Random floating point number:", random.random())

c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
print("Random floating point number between c and d:", random.uniform(c, d))

mu = int(input("Enter the value of mu: "))
sigma = int(input("Enter the value of sigma: "))
print("Random number from normal distribution:", random.normalvariate(mu, sigma))

k = int(input("Enter the value of k: "))
print("Random integer with k random bits:", random.getrandbits(k))

alpha = int(input("Enter the value of alpha: "))
beta = int(input("Enter the value of beta: "))
print("Random number from beta distribution:", random.betavariate(alpha, beta))

alpha1 = int(input("Enter the value of alpha: "))
beta1 = int(input("Enter the value of beta: "))
print("Random number from gamma distribution:", random.betavariate(alpha1, beta1))
