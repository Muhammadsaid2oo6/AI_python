import numpy as np 

x  = np.array([[1,2], [3,4]], dtype=np.float64)
y  = np.array([[4,5], [6,7]], dtype=np.float64)

print(x+y)
print(np.add(x,y))

print("\n")

print(x-y)
print(np.subtract(x,y))

print("\n")

print(x*y)
print(np.multiply(x,y))

print("\n")

print(x/y)
print(np.divide(x,y))

print("\n")

print(np.sqrt(x))

print("\n")

print(np.power(x))

print("\n")

print(np.sum(x*y))