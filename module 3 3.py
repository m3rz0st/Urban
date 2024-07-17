def print_params(a=1, b='строка', c=True):
    print(a, b, c)


value_list = [1, 'bool', False]
value_dict = {'a': 142, 'b': 'коляска', 'c': None}
# print_params(*value_list, **value_dict) - будет ошибка, так как параметров больше, чем можно передать
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

