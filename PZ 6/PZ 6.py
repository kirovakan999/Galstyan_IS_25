# Вариант 6
# Даны пелыс числа N (2), А и В. Сформировать и вывести полочисленный список размера 10, первый элемент которого равен А, второй равен В, а каждый последующий элемент равен сумме всех предыдущих. python
def generate_sequence(a, b, n):
    sequence = [a, b]  # инициализируем список первыми двумя числами

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]  # вычисляем следующее число как сумму двух предыдущих
        sequence.append(next_number)  # добавляем вычисленное число в список

    return sequence  # возвращаем полученный список


# Вводим значения
a = int(input("Введите значение А: "))
b = int(input("Введите значение B: "))
n = 10  # задаем размер последовательности, равный 10 (как указано в задании)

# Формируем и выводим последовательность
result_sequence = generate_sequence(a, b, n)
print(result_sequence)