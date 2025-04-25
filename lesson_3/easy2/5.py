# def interleave(list1, list2):
#     new_list = [item for sets in list(zip(list1, list2)) for item in sets]
#     return new_list

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]


def interleave(list1, list2):
    new_list = []
    for idx in range(len(list1)):
        new_list.append(list1[idx])
        new_list.append(list2[idx])

    return new_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2))    # True