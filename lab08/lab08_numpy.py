import numpy as np

# ============================================================
# Задание 1. Создание векторов и матриц
# ============================================================
print("=" * 50)
print("Задание 1. Создание векторов и матриц")
print("=" * 50)

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours =", hours)
print("line =", line)
print("zeros =", zeros)
print("unknown_table =")
print(unknown_table)
print("identity =")
print(identity)

print("hours.shape =", hours.shape)
print("hours.ndim  =", hours.ndim)
print("hours.size  =", hours.size)
print("hours.dtype =", hours.dtype)

# ============================================================
# Задание 2. Индексы и срезы в векторе
# ============================================================
print("=" * 50)
print("Задание 2. Индексы и срезы в векторе")
print("=" * 50)

print("Третий элемент (индекс 2):", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

# ============================================================
# Задание 3. Строки и столбцы таблицы
# ============================================================
print("=" * 50)
print("Задание 3. Строки и столбцы таблицы")
print("=" * 50)

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2×2:")
central = temperatures[0:2, 1:3]
print(central)
print("Форма центрального фрагмента:", central.shape)

# ============================================================
# Задание 4. Прямоугольные срезы
# ============================================================
print("=" * 50)
print("Задание 4. Прямоугольные срезы")
print("=" * 50)

matrix = np.arange(1, 26).reshape(5, 5)
print("matrix =")
print(matrix)

first_three = matrix[:3]
print("Первые три строки (shape %s):" % (first_three.shape,))
print(first_three)

last_two = matrix[-2:]
print("Последние две строки (shape %s):" % (last_two.shape,))
print(last_two)

first_two_cols = matrix[:, :2]
print("Первые два столбца (shape %s):" % (first_two_cols.shape,))
print(first_two_cols)

fragment = matrix[1:4, 2:5]
print("Строки 1–3, столбцы 2–4 (shape %s):" % (fragment.shape,))
print(fragment)

corner = matrix[-2:, -2:]
print("Угловой блок 2×2 правый нижний (shape %s):" % (corner.shape,))
print(corner)

# ============================================================
# Задание 5. Изменение массива с помощью срезов
# ============================================================
print("=" * 50)
print("Задание 5. Изменение массива с помощью срезов")
print("=" * 50)

# Примеры из условия
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после изменения:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после изменения:")
print(small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99 
changed_hours[0::2] = -1 
print("changed_hours:", changed_hours)
print("hours (не изменился):", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:")
print(changed_matrix)
print("matrix (не изменилась):")
print(matrix)

# ============================================================
# Задание 6. Изменение формы
# ============================================================
print("=" * 50)
print("Задание 6. Изменение формы")
print("=" * 50)

numbers = np.arange(12)
table = numbers.reshape(3, 4) 
transposed = table.T

print("numbers.shape =", numbers.shape)
print("table.shape =", table.shape)
print("transposed.shape =", transposed.shape)
print("table =")
print(table)
print("transposed =")
print(transposed)