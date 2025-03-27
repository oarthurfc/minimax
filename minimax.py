def max_min_select(arr, left, right):
    # Caso base: Apenas um elemento na lista
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: Dois elementos, comparando diretamente
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Dividindo o array ao meio
    mid = (left + right) // 2
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
    
    # Combinando os resultados das subárvores
    return min(min1, min2), max(max1, max2)

# Testando o algoritmo
arr = [12, 4, 56, 19, 8, 23, 89, 5]
min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
print(f"Menor valor: {min_val}, Maior valor: {max_val}")
