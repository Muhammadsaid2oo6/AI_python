import numpy as np

x = np.array([2.5,5.1,3.2,8.5,3.5,1.5,9.2,5.5,8.3,2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,4.8,3.8,6.9,7.8])
y = np.array([21,47,27,75,30,20,88,60,81,25,85,62,41,42,17,95,30,24,67,69,30,54,35,76,86])


n = len(x)

a = (np.sum(y)*np.sum(np.power(x,2))-np.sum(x)*np.sum(x*y))/(n*np.sum(np.power(x,2))-np.power(np.sum(x),2))
b = (n*np.sum(x*y)-np.sum(x))*np.sum(y)/(n*np.sum(np.power(x,2))-np.sum(np.power(x,2)))
y1 = a*x+b
e = 1/n*np.sum(np.power(y-y1,2))

print("e=", e)


