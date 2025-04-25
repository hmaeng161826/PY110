def dms(number):
    deg_whole_num, remainder_from_degree = divmod(number, 1)
    min_whole_num, remainder_from_min = divmod(remainder_from_degree, 1)
    sec = remainder_from_min * 60

    return f'{deg_whole_num}, {min_whole_num}, {sec}'



print(dms(254.6))
