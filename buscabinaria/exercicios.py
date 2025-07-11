# -QUICKSORT
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# EXERCÍCIO 1
def busca_linear(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
        elif num > target:
            return i
    return len(arr)

def busca_binaria(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# EXERCÍCIO 2
def indice_h_linear(citacoes):
    h = 0
    for i, c in enumerate(citacoes):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

def indice_h_binaria(citacoes):
    n = len(citacoes)
    left, right = 0, n - 1
    h = 0
    while left <= right:
        mid = (left + right) // 2
        if citacoes[mid] >= mid + 1:
            h = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return h

# TESTANDO EXERCÍCIO 1
arr = [3, 8, 2, 5, 1, 9]
target = 7
sorted_arr = quicksort(arr)
print("Array ordenado:", sorted_arr)
print("Busca Linear:", busca_linear(sorted_arr, target))
print("Busca Binária:", busca_binaria(sorted_arr, target))

# TESTANDO EXERCÍCIO 2
citacoes = [10, 8, 5, 4, 3]
print("Índice-h Linear:", indice_h_linear(citacoes))
print("Índice-h Binária:", indice_h_binaria(citacoes))
