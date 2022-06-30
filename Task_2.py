# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
#  и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]


list_numbers = [1,5, 2, 3, 4, 6, 1, 7]


def increase_sequence(list_numbers, index=0, continue_with=0):
    sequence = []
    last = index
    sequence.append(list_numbers[last])
    for i in range(last + continue_with, len(list_numbers)):
        if list_numbers[i] > list_numbers[last]:
            last = i
            sequence.append(list_numbers[i])
        
    return sequence


increase_sequence(list_numbers)


def max_increase_sequence(list_numbers):
    max_sequence = []
    for i in range(0, len(list_numbers)):
        for j in range(1, len(list_numbers)):
            sequence = increase_sequence(list_numbers, index=i,continue_with=j)
            # print(f'{i=}, {j=}, {sequense}')
            lenght= len(sequence)
            if lenght > len(max_sequence):
                max_sequence = sequence

    return max_sequence



print(max_increase_sequence(list_numbers))
