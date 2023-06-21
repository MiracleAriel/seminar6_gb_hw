# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты расстановок

import random

def queens_are_safe(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

def generate_random_queens():
    queens = []
    for _ in range(8):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        queens.append((x, y))
    return queens

successful_arrangements = []
attempts = 0

while len(successful_arrangements) < 4 and attempts < 1000:
    queens = generate_random_queens()
    if queens_are_safe(queens):
        successful_arrangements.append(queens)
    attempts += 1

# Вывод успешных расстановок
for i, arrangement in enumerate(successful_arrangements):
    print(f"Successful arrangement {i+1}:")
    for queen in arrangement:
        print(queen)
    print()
