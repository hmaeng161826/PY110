def multiplicative_average(lst):
    multiplied_number = 1
    for number in lst:
        multiplied_number *= number
    product_average = multiplied_number / len(lst)
    result_string = f'{product_average:.3f}'
    return result_string

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")