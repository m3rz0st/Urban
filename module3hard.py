def calculate_structure_sum(data):
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return len(data)
    if isinstance(data, list) or isinstance(data, tuple):
        if len(data) == 0:
            return 0
        return calculate_structure_sum(data[0]) + calculate_structure_sum(data[1:])
    if isinstance(data, dict):
        return calculate_structure_sum(list(data.items()))
    if isinstance(data, set):
        return calculate_structure_sum(list(data))


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)









