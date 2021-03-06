# Módulo adicional - Otimização heurística

## TODO

Configurem os algoritmos de maneira que eu possa executá-los de forma ideal. Os parâmetros estão localizados na parte de configuração da suíte de testes

As funções em comum já estão num arquivo chamado utilities.py

Padronizar os comentários em português

Reorganizar o módulo

Se sobrar tempo, testaremos com: 25, 50, 100, 250 iterações

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

```python
import unittest
class SearchTests(unittest.TestCase):

    def setUp(self):
        self.Vector = [1, 2]
        self.TSP = []
        self.TSP.insert(0, [7542, readtsplib.readData('TSPLIB/berlin52.tsp')])
        self.TSP.insert(1, [26524, readtsplib.readData('TSPLIB/kroa150.tsp')])
        self.TSP.insert(2, [22141, readtsplib.readData('TSPLIB/krob100.tsp')])
        self.TSP.insert(3, [44303, readtsplib.readData('TSPLIB/pr107.tsp')])
        self.TSP.insert(4, [108159, readtsplib.readData('TSPLIB/pr76.tsp')])

```
Cada função de teste das três metaheurísticas roda o algoritmo **10** vezes. Algumas configurações do setup podem ser alteradas na suíte de testes

Rodando o script no terminal:
```
$ python3 test_suite.py
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