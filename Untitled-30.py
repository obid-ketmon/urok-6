#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def generate_arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

def main():
    try:
        a1 = float(input("Введите первый элемент прогрессии (a1): "))
        d = float(input("Введите разность прогрессии (d): "))
        n = int(input("Введите количество элементов прогрессии: "))

        if n <= 0:
            print("Количество элементов должно быть положительным.")
            return

        progression = generate_arithmetic_progression(a1, d, n)

        print("Арифметическая прогрессия:")
        for element in progression:
            print(element)

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа корректно.")

if __name__ == "__main__":
    main()
