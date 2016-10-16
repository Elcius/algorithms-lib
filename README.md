# Biblioteca de otimização - APA 2016.1 - Python 3
##### Samuel Pordeus - Elcius Ferreira - Victor Franco
A biblioteca contém 15 algoritmos de otimização, 9 de programação dinâmica e 6 algoritmos gulosos, abaixo podemos ver os algoritmos contidos e quem os implementou.

#### Guidelines
A biblioteca segue os padrões de código em **Python** da [**PEP8**](https://www.python.org/dev/peps/pep-0008/)

### 1. Designação dos algoritmos
#### **_Samuel Pordeus_**
##### **Dinâmicos**
1. Mochila binária
2. Maior subsequência comum
3. Distância de edição

##### **Gulosos**
1. Caminho mais curto (Algoritmo de Dijkstra)
2. Coloração de grafos

#### **_Elcius Ferreira_**
##### **Dinâmicos**
1. Triângulo de Pascal
2. Soma de subconjunto
3. Multiplicação de matrizes

##### **Gulosos**
1. Seleção de atividades
2. Mochila fracionária

#### **_Victor Franco_**
##### **Dinâmicos**
1. Quebra de palavras
2. Troco em moedas
3. Empilhamento de caixas

##### **Gulosos**
1. Árvore geradora mínima (Algoritmo de Kruskal)
2. Árvore geradora mínima (Algoritmo de Prim)

### 2. Testes
* Um conjunto de testes para cada algoritmo foi desenvolvido e está no script test.py.
* Para testar os algoritmos basta remover os comentários na chamada das funções de teste que desejar visualizar

### 3. Algoritmos
Os algoritmos estão implementados de forma que pode-se chamá-los por duas funções:
```python
import algorithms
# Se chamados pela funcao com 'call' antes, os algoritmos chamam a funcao original
# e printam a saída detalhadamente
algorithms.call_edit_distance(str1, str2)
# Podemos chamar as funcoes otimizadas diretamente utilizando seus parametros originais
algorithms.edit_distance(str1, str2, len(A), len(B))
```
#### 3.1 Programação dinâmica
###### Mochila binária
```python
import algorithms
# A entrada é a capacidade da mochila, o peso dos itens e o valor dos itens
# Se for mais de um item, deve-se colocá-los em listas de tamanhos iguais.
# n é a quantidade de valores inseridos, preferencialmente colocar len(value) ou len(weight)
algorithms.max_knapsack.py(cap, weight, value, n)
# A saída é o valor máximo da mochila
```
A algoritmo da mochila binária pega itens que contém pesos e valores e coloca o máximo de valor possível mediante a capacidade da mochila. Teve sua aplicação principal no algoritmo de **Criptografia de chave pública**.
* Complexidade O(2^n)

###### Maior subsequência comum
```python
import algorithms
# A entrada são as duas strings que serão comparadas e o tamanho respectivo destas
algorithms.lcs(str1, str2, A, B)
# A saída é o valor inteiro da maior subsequência comum
```
O algoritmo da maior subsequência comum analisa duas strings e visualiza qual o tamanho da maior sequencia comum entre elas. Entre as suas aplicações estão a _engine_ da **wiki** e **sistemas de controle de versão**.
* Complexidade O(2^n)

###### Distância de edição
```python
import algorithms
# A entrada são as duas strings que serão comparadas e o tamanho respectivo destas
algorithms.edit_distance(str1, str2, m, n)
# A saída é o valor inteiro do número de operações necessárias para convertar str1 em str2
```
O algoritmo da distância de edição pega duas strings e as compara para saber quantas operações seriam necessárias para que uma string se tornasse a outra.
* Complexidade O(m x n) - Sendo m o tamanho de uma string e n o de outra

###### Triângulo de pascal
```python
import algorithms
# A entrada são dois inteiros, n representa o número da linha e k o da coluna
algorithms.binomial_coefficient(n, k)
# A saída é o valor inteiro do coeficiente binomial do triângulo de pascal
```
O algoritmo pega o número de linhas e de colunas e cálcula pelo triângulo de pascal
o coeficiente binomial. Esse algoritmo é utilizado na matemática.
* Complexidade O(n x k)

###### Soma de subconjunto
```python
import algorithms
# A entrada é um array de números e a soma a ser analisada
algorithms.is_subset_sum(set, sum)
# A saída é um booleano dizendo se a soma está contida ou não.
```
O algoritmo confere se em um dado set de números, um número inteiro está contido na soma de números deste set.

* Complexidade O(sum x n)

###### Multiplicação de matrizes
```python
import algorithms
# A entrada é um array de números e o tamanho dela.
matrix_chain_order(arr, n)
# A saída é a menor quantidade possível de múltiplicações das matrizes
```
O algoritmo dá a forma mais eficiente de multiplicar as matrizes de tamanho indicado

* Complexidade O(n³)

#### 3.2 Algoritmos gulosos
###### Caminho mais curto (Algoritmo de Dijkstra)
```python
import algorithms
# A entrada é o grafo, que é representado por um dict e o vértice que será comparado aos outros
graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
algorithms.shortest_path(graph, start)
# A saída é uma lista com os valores sequenciais do caminho mais curto
# de cada vértice para o vértice indicado em start
```

O algoritmo do caminho mais curto de Dijkstra mede o caminho mais curto entre um ponto e outro, sua aplicação
é vastamente utilizada na programação, como em problemas de **Redes telefônicas** ou **Controle de aeronaves**
* Complexidade O(V²)

###### Coloração de Grafos
```python
import algorithms
# A entrada é o grafo, que é representado por um dicionário e as cores que serão dadas aos grafos
graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
algorithms.colored_graphs(graphs, colors)
# A saída é a respectiva cor de cada vértice do grafo
```
O algoritmo da distância de edição pega duas strings e as compara para saber quantas operações seriam necessárias para que uma string se tornasse a outra.
* Complexidade O(V² + E)

###### Seleção de atividades
```python
import algorithms
# A entrada são as duas lista, start e finish
algorithms.max_activities(s, f)
# A saída é uma lista indicando quais atividades podem ser executadas por uma única pessoa
```
O algoritmo seleciona o máximo número de atividades possíveis, mediante o tempo de começo e fim destas,
que podem ser realizadas por uma única pessoa. Dentre as aplicações estão algoritmos para otimizar
rotinas.

###### Mochila fracionária
```python
import algorithms
# A entrada é a capacidade da mochila, uma listas do objeto item
# que contém peso e valor e o tamanho da lista
items_list = [algorithms.Item(60, 10), algorithms.Item(40, 10), algorithms.Item(50, 30)]
algorithms.fractional_knapsack(W, items_list, n)
# A saída é o valor máximo da mochila
```
A algoritmo da mochila binária pega itens que contém pesos e valores e coloca o máximo de valor possível mediante a capacidade da mochila. Ao contrário do algoritmo da Mochila Binária, aqui podemos quebrar os valores em várias partes, agilizando o algoritmo.
* Complexidade O(n x log n)
