# Módulo adicional - Otimização heurística
##### Samuel Pordeus - Elcius Ferreira - Victor Franco

A biblioteca contém 3 abordagens metaheurísticas para resolução do **_Problema do Caixeiro Viajante_**

#### Guidelines
A biblioteca segue os padrões de código de **Python** da [**PEP8**](https://www.python.org/dev/peps/pep-0008/)

### 1. Designação das metaheurísticas
### **Samuel Pordeus**
GRASP

### **Elcius Ferreira**
Variable Neighborhood Search

### **Victor Franco**
Tabu Search

### 2. Testes
Um conjunto de testes para cada algoritmo foi desenvolvido e é executado se você rodar o script de teste do algoritmo em questão.
Para a criação dos testes automatizados, utilizamos o módulo [**unittest**](https://docs.python.org/3/library/unittest.html).

Exemplo, algoritmo da Maior Subsequência Comum (LCS):
```python
import unittest
class SearchTests(unittest.TestCase):

    def setUp(self):
        self.Vector = [1, 2]
        TSP = []
        TSP.insert(0, readtsplib.readData('TSPLIB/pr107.tsp'))
        TSP.insert(1, 44303)
        self.TSPDATA = TSP[0]
        self.TSPBEST = TSP[1]
```
Rodando o script no terminal:
```
$ python3 TestPr107.py
```
---
### 3. Arquivos de entrada
Utilizamos as entradas da TSPLib e fizemos uma função para adaptar os arquivòs da biblioteca para uma estrutura de dados adequada. Optamos por utilizar listas.

**berlin52.tsp**
- distância ideal: 7542 passos

**kroa150.tsp**
- distância ideal: 26524 passos

**krob100.tsp**
- distância ideal: 22141 passos

**pr107.tsp**
- distância ideal: 44303 passos

**pr76.tsp**
- distância ideal: 108159 passos