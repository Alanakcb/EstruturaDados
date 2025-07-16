#Exercicio usando Força Bruta
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


#Exercício usando quicksort
def two_sum(nums, target):
    arr = []
    for idx in range(len(nums)):
        num = nums[idx]
        arr.append((num, idx))

    quicksort(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        soma = arr[left][0] + arr[right][0]
        if soma == target:
            return [arr[left][1], arr[right][1]]
        elif soma > target:
            right -= 1
        else:
            left += 1

    return []

#Exercício usando hash map
def two_sum(numeros, alvo):
    indice_por_valor = {}

    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i

if __name__ == "__main__":
    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum(numeros, alvo)
    print(resultado)