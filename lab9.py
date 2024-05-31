#Напишіть програму, яка реалізує класичний алгоритм сортування рядків двовимірного масиву методом злиття.
#Розмірність масиву та всі елементи вводяться з клавіатури.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
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


dimensions = input("Введіть розмірність масиву (наприклад, 3 3 для масиву 3x3): ")
rows, cols = map(int, dimensions.split())

print("Введіть елементи масиву:")
matrix = []
for _ in range(rows):
    row = input().split()
    matrix.append(row)

for i in range(rows):
    matrix[i] = merge_sort(matrix[i])

print("Відсортований масив:")
for row in matrix:
    print(' '.join(row))

