# a = int(input(">>> "))
# if (a < 10 and a > 5) or (a % 2 == 0):
#     print(True)
# else:
#     print(False)


# letter = input(">>> ")
# def check_letter(letter):
#     unli = ['a', 'e', 'i', 'o', 'u', 'y']
#     undosh = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g',
#               'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
#     if letter.lower() in unli:
#         return 'unli'
#     elif letter.lower() in undosh:
#         return 'undosh'
#     else:
#         return 'only_LETTERS'

# print(check_letter(letter))

# list1 = list(range(1, 101))
# list2 = list(range(101, 201))

# sum_l = []
# for i in range(len(list1)):
#     sum_l.append(list1[i] + list2[i])

# print(sum_l)
    
import random

list1 = [random.randint(1, 100) for x in range(100)]
list2 = [random.randint(1, 100) for x in range(100)]

sum_list = []
i = 0
while i < len(list1):
    sum_list.append(list1[i]+list2[i])
    i += 1
    
print(sum_list)

