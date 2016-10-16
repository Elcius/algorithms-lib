# Biblioteca de otimização - APA 2016.1 - Python 3
##### Samuel Pordeus - Elcius Ferreira - Victor Franco
A biblioteca contém 15 algoritmos de otimização, 9 de programação dinâmica e 2 algoritmos gulosos, abaixo podemos ver os algoritmos contidos e quem os implementou.

#### 1. Designação dos algoritmos
##### **_Samuel Pordeus_**
* **Dinâmicos**
1. Mochila binária
2. Maior subsequência comum
3. Distância de edição
* **Gulosos**
1. Caminho mais curto (Algoritmo de Dijkstra)
2. Coloração de grafos

##### **_Elcius Ferreira_**
* **Dinâmicos**
1. Triângulo de Pascal
2. Soma de subconjunto
3. Multiplicação de matrizes
* **Gulosos**
1. Seleção de atividades
2. Mochila fracionária

##### **_Victor Franco_**
* **Dinâmicos**
1.
2.
3.
* **Gulosos**
1.
2.

#### 2. Testes
* Um conjunto de teste para cada algoritmo foi desenvolvido e está no script test.py.
* Para testar os algoritmos basta remover os comentários na chamada das funções de teste que desejar visualizar

#### 3. Algoritmos
Os algoritmos estão implementados de forma que pode-se chamá-los por duas funções:
```python
import algorithms
# Se chamados pela funcao com 'call' antes, os algoritmos chamam a funcao original
# e printam a saída detalhadamente
algorithms.call_edit_distance(str1, str2)
# Podemos chamar as funcoes otimizadas diretamente utilizando seus parametros originais
algorithms.edit_distance(str1, str2, len(A), len(B))
```
##### 3.1 Programação dinâmica
###### Mochila binária
