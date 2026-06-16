from math import comb

n = 5
x = 3
p = 0.5

probabilidad = comb(n,x)*(p**x)*((1-p)**(n-x))

print("Probabilidad:", probabilidad)
