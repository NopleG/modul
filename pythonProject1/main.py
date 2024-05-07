import numpy as np

def main():
    # Ввод размерности матрицы
    n = int(input("Введите количество строк (N): "))
    m = int(input("Введите количество столбцов (M): "))

    # Создание пустой матрицы
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input(f"Введите элемент [{i+1}, {j+1}]: ")))
        matrix.append(row)

    # Печать матрицы
    print("Ваша матрица:")
    for row in matrix:
        print(row)

    # Нахождение суммы элементов на главной диагонали
    main_diag_sum = sum(matrix[i][i] for i in range(min(n, m)))

    # Нахождение суммы элементов на побочной диагонали
    side_diag_sum = sum(matrix[i][m - 1 - i] for i in range(min(n, m)))
    # Нахождение минимального элемента и его индексов
    min_element = matrix[0][0]
    min_row_index = min_col_index = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row_index = i
                min_col_index = j


    # Вывод результатов
    print(f"Сумма элементов на главной диагонали: {main_diag_sum}")
    print(f"Сумма элементов на побочной диагонали: {side_diag_sum}")
    # Вычисление определителя матрицы
    determinant = np.linalg.det(matrix)

    # Вывод результата
    print(f"Определитель матрицы: {determinant}")

    # Вывод результата
    print(f"Минимальный элемент: {min_element}")
    print(f"Индексы минимального элемента: [{min_row_index + 1}, {min_col_index + 1}]")

main()