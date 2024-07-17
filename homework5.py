immutable_var = 1, 'str', 2.5
print(immutable_var)
# нельзя изменить элементы потому, что элемент в кортеже нельзя
# менять без наличия отдельного списка

mutable_list = [1, 'str', True]
mutable_list[0] = 5
print(mutable_list)