#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_elements_in_range(input_list, min_value, max_value):
    indices = []
    for i, element in enumerate(input_list):
        if min_value <= element <= max_value:
            indices.append(i)
    return indices

def main():
    try:
        # Ввод списка
        input_list = input("Введите элементы списка через пробел: ").split()
        input_list = [float(item) for item in input_list]  # Преобразуем в список чисел

        # Ввод минимального и максимального значения диапазона
        min_value = float(input("Введите минимальное значение диапазона: "))
        max_value = float(input("Введите максимальное значение диапазона: "))

        # Поиск индексов элементов, удовлетворяющих условию
        indices = find_elements_in_range(input_list, min_value, max_value)

        # Вывод результатов
        if indices:
            print("Индексы элементов, удовлетворяющих диапазону:")
            print(indices)
        else:
            print("В списке нет элементов, удовлетворяющих заданному диапазону.")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа корректно.")

if __name__ == "__main__":
    main()
