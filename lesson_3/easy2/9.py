def count_occurrences(list):
    count_history_dict = {}
    for item in list:
        if item in count_history_dict:
            count_history_dict[item] += 1
        else:
            count_history_dict [item] = 1
    for key, value in count_history_dict.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)