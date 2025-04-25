def digit_list(number):
    list_strings = list(str(number))
    list_numbers = [int(string) for string in list_strings]
        
    return list_numbers

print(digit_list(12345))     # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
