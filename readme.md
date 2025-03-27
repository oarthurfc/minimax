# Projeto: Algoritmo de Seleção Simultânea do Maior e Menor Elemento (MaxMin Select)

## Descrição do Projeto

Este projeto implementa o **algoritmo de seleção simultânea do maior e menor elemento (MaxMin Select)**, utilizando a abordagem de **divisão e conquista**. Esse algoritmo permite encontrar simultaneamente o maior e o menor elemento de um conjunto de números de forma eficiente, reduzindo o número de comparações em relação a uma abordagem ingînua.

### Lógica do Algoritmo

O algoritmo **MaxMin Select** segue a abordagem de **divisão e conquista**, onde a sequência é dividida em partes menores, e os valores máximos e mínimos são combinados recursivamente.

#### **Passos do Algoritmo:**
1. **Caso base:** Se houver apenas um elemento, ele é tanto o maior quanto o menor.
2. **Comparando pares:** Se houver dois elementos, um é o maior e o outro é o menor.
3. **Divisão recursiva:** O conjunto é dividido ao meio, e os máximos e mínimos de cada metade são encontrados recursivamente.
4. **Combinação:** O menor dos dois valores mínimos é selecionado como o menor geral, e o maior dos dois valores máximos é escolhido como o maior geral.

## Explicação do Código
A implementação do **MaxMin Select** segue os seguintes passos:

1. **Definição da função recursiva:**
   ```python
   def maxmin_select(arr, left, right):
   ```
   - A função recebe um array e os índices `left` e `right` para dividir a sequência.

2. **Caso base:**
   ```python
   if left == right:
       return arr[left], arr[left]
   ```
   - Se houver apenas um elemento, ele é retornado como maior e menor.

3. **Comparando dois elementos:**
   ```python
   if right == left + 1:
       return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
   ```
   - Se houver dois elementos, eles são comparados diretamente.

4. **Dividindo a sequência:**
   ```python
   mid = (left + right) // 2
   min1, max1 = maxmin_select(arr, left, mid)
   min2, max2 = maxmin_select(arr, mid + 1, right)
   ```
   - O array é dividido ao meio, e o algoritmo é chamado recursivamente.

5. **Combinando os resultados:**
   ```python
   return min(min1, min2), max(max1, max2)
   ```
   - O menor dos dois valores mínimos e o maior dos dois valores máximos são selecionados.

6. **Executando o algoritmo:**
   ```python
   numbers = [3, 1, 5, 2, 4, 8, 7]
   min_val, max_val = maxmin_select(numbers, 0, len(numbers) - 1)
   print(f"Menor: {min_val}, Maior: {max_val}")
   ```
   - O algoritmo é chamado para encontrar o menor e o maior elemento do conjunto.

## Como Executar o Projeto

### Requisitos
- 🐍 Python 3.x instalado

### Executando o Código
1. 📥 Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/maxmin-select.git
   cd maxmin-select
   ```
2. ▶️ Execute o script principal:
   ```sh
   python main.py
   ```
3. 🔍 O menor e o maior número da lista serão exibidos.

## Complexidade Assintótica

A complexidade do algoritmo pode ser analisada pela relação de recorrência:

\[
T(n) = 2T(n/2) + O(1)
\]

### **Cálculo pelo Teorema Mestre**
1. **Identificando os valores:**
   - \( a = 2 \), \( b = 2 \), \( f(n) = O(1) \)

2. **Cálculo de \( log_b a \):**
   - \( p = log_2 2 = 1 \)

3. **Determinação do caso do Teorema Mestre:**
   - \( f(n) = O(1) = O(n^0) \) com \( c = 0 \) e \( p = 1 \), então **o caso 1 se aplica**.

4. **Solução assintótica:**
   - \( T(n) = O(n) \)

## Conclusão

- **O algoritmo MaxMin Select encontra simultaneamente o maior e o menor elemento da lista usando divisão e conquista.**
- **Reduz o número de comparações em relação a uma abordagem ingînua.**
- **Tem complexidade O(n), tornando-se eficiente para listas grandes.**

## Referências

- 📚 [Valor máximo e mínimo de um veto - Blog Cyberini](https://www.blogcyberini.com/2017/09/maximo-e-minimo-de-um-vetor.html)
- 📚 [Divisão e Conquista - GeeksforGeeks](https://www.geeksforgeeks.org/divide-and-conquer/)
