def find_pairs(first_number):
    for second_number in range(1, 20 + 1):
        if first_number % (second_number + 1) == 0:
            yield f"{first_number} {second_number}"


first_number = int(input("Введите первое число: "))


while first_number <= 20:
    print( * find_pairs(first_number), sep='\n')
    first_number += 1


