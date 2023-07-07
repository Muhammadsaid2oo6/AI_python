
import random

list1 = [random.randint(1, 100) for x in range(100)]
list2 = [random.randint(1, 100) for x in range(100)]

sum_list = []
i = 0

while i < len(list1):
    sum_list.append(list1[i]+list2[i])
    i += 1

print(sum_list)
