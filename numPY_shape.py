import numpy as np

# b = np.array([[1,2,3,4], [5,6,7,8]])

# print(b.reshape(4,2))

#=============== RANDOM =====================

# c = np.random.randint(1,10,(2,5))

# h = np.mean(c,axis=0)

# print(h)

#=============== append =====================


import numpy as np

b = np.random.randint(2, 5, (5, 2))
c = np.random.randint(1, 10, size=(5, 2))
l = [[], []]

for i in range(len(b[0])):
    for j in range(len(b)):
        l[i].append(b[j][i])


print(l_array)







