def halvsies(lst):
    list1 = []
    list2 = []

    half_point = (len(lst) + 1) // 2
    list1 = lst[:half_point]
    list2 = lst[half_point:]
    new_list = [list1, list2]
    return new_list

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
