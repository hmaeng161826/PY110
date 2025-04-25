# def union(list1, list2):
#     combined_list = list1 + list2
#     set_combined_list = set(combined_list)
#     return set_combined_list



def union(list1, list2):
    set_numbers = set(list1) | set(list2)
    return set_numbers

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True