import random
# Практика 1
def bubble_sort(arr):
    """Сортировка пузырьком"""
    array = arr[:]
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(arr):
    """Сортировка выбором"""
    array = arr[:]
    n = len(array)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def insertion_sort(arr):
    """Сортировка вставками"""
    array = arr[:]
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


original_array = [random.randint(-50, 50) for _ in range(15)]
print(f"Исходный массив: {original_array}")


print("Сортировка пузырьком:", bubble_sort(original_array.copy()))
print("Сортировка выбором:", selection_sort(original_array.copy()))
print("Сортировка вставками:", insertion_sort(original_array.copy()))

#Практика 2

def merge_sort(arr):
    """Сортировка слиянием"""
    if len(arr) <= 1:
        return arr[:]
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Слияние
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def sort_strings_by_length(strings):
    """Сортировка строк по длине слова"""
    return sorted(strings, key=len)



numbers = [random.randint(0, 1000) for _ in range(20)]
print(f"Исходные числа: {numbers}")

merge_sorted = merge_sort(numbers.copy())
builtin_sorted = sorted(numbers.copy())

print(f"\nСортировка слиянием: {merge_sorted}")
print(f"Встроенная sorted(): {builtin_sorted}")
print(f"Результаты совпадают? {merge_sorted == builtin_sorted}")


strings = ["алгоритм", "код", "программа", "сортировка", 
           "массив", "бинарный", "поиск"]
print(f"Исходные строки: {strings}")


sorted_strings = sort_strings_by_length(strings.copy())
print(f"Строки, отсортированные по длине: {sorted_strings}")

#Практика 3

def average(grades_list):
    """Вычисление средней оценки"""
    return sum(grades_list) / len(grades_list) if grades_list else 0


# Создаем список студентов
students = [
    {'name': 'Леонов Максим', 'group': 'ИСП-1-9-24', 'grades': [4, 4, 3, 5]},
    {'name': 'Булгакова Полина', 'group': 'ИСП-1-9-24', 'grades': [5, 5, 5, 4]},
    {'name': 'Алексей Рогозин', 'group': 'ИСП-1-9-24', 'grades': [5, 4, 4, 4]},
    {'name': 'Роман Швец', 'group': 'ИСП-1-9-24', 'grades': [5, 4, 4, 3]},
    {'name': 'Куркин Евгений', 'group': 'ИСП-1-9-24', 'grades': [4, 4, 4, 4]},
    {'name': 'Триппель Максим', 'group': 'ИСП-1-9-24', 'grades': [5, 5, 4, 4]},
    {'name': 'Харитонова Наталия', 'group': 'ИСП-1-9-24', 'grades': [5, 5, 4, 4]},
    {'name': 'Дейнека Антон', 'group': 'ИСП-2-9-24', 'grades': [4, 5, 4, 4]},
]

while True:
    print("\nМеню:")
    print("1. Вывести список студентов (в исходном порядке)")
    print("2. Отсортировать по ФИО (по алфавиту)")
    print("3. Отсортировать по средней оценке (по убыванию)")
    print("4. Отсортировать по номеру группы (по возрастанию), а внутри группы по ФИО")
    print("5. Найти студента с максимальной средней оценкой")
    print("6. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        print("\nСписок студентов (исходный порядок):")
        for i, student in enumerate(students, 1):
            avg = average(student['grades'])
            print(f"{i}. {student['name']} ({student['group']}) - средний балл: {avg:.2f}")
    
    elif choice == '2':
        sorted_students = sorted(students, key=lambda s: s['name'])
        print("\nСтуденты, отсортированные по ФИО:")
        for i, student in enumerate(sorted_students, 1):
            avg = average(student['grades'])
            print(f"{i}. {student['name']} ({student['group']}) - средний балл: {avg:.2f}")
    
    elif choice == '3':
        sorted_students = sorted(students, 
                                 key=lambda s: average(s['grades']), 
                                 reverse=True)
        print("\nСтуденты, отсортированные по средней оценке:")
        for i, student in enumerate(sorted_students, 1):
            avg = average(student['grades'])
            print(f"{i}. {student['name']} ({student['group']}) - средний балл: {avg:.2f}")
    
    elif choice == '4':
        sorted_students = sorted(students, key=lambda s: (s['group'], s['name']))
        print("\nСтуденты, отсортированные по группе и ФИО:")
        for i, student in enumerate(sorted_students, 1):
            avg = average(student['grades'])
            print(f"{i}. {student['name']} ({student['group']}) - средний балл: {avg:.2f}")
    
    elif choice == '5':
        best_student = max(students, key=lambda s: average(s['grades']))
        avg = average(best_student['grades'])
        print(f"\nСтудент с максимальной средней оценкой:")
        print(f"Имя: {best_student['name']}")
        print(f"Группа: {best_student['group']}")
        print(f"Средний балл: {avg:.2f}")
    
    elif choice == '6':
        print("Выход из программы.")
        break
    
    else:
        print("Ошибка! Пожалуйста, выберите действие от 1 до 6.")
