import math


def find_pythagorean_triplets(list1):
    list.sort()
    for i in range(len(list1)):
        for j in range(len(list1)):
            if math.sqrt(list1[i]**2 + list1[j]**2) in list1:
                return [list1[i], list1[j], math.sqrt(list1[i]**2 + list1[j]**2)]
    return -1


def find_pythagorean_triplets_three_loops(list1):
    list1.sort()
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            for k in range(j+1, len(list1)):

                if list1[i]**2 + list1[j]**2 == list1[k]**2:
                    return True
    return False


print(find_pythagorean_triplets_three_loops([1, 2, 3, 4, 5, 6, 7]))
print(find_pythagorean_triplets_three_loops([4]))

# print(find_pythagorean_triplets_three_loops([12, 1, 3]))
