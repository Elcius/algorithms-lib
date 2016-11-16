# Módulo adicional - Otimização heurística
##### Samuel Pordeus - Elcius Ferreira - Victor Franco

A biblioteca contém 3 abordagens metaheurísticas para resolução do **_Problema do Caixeiro Viajante_**

#### Guidelines
A biblioteca segue os padrões de código de **Python** da [**PEP8**](https://www.python.org/dev/peps/pep-0008/)

### 1. Designação das metaheurísticas
#### **_Samuel Pordeus_**
GRASP

#### **_Elcius Ferreira_**
Variable Neighborhood Search

#### **_Victor Franco_**
Tabu Search

### 2. Testes
Um conjunto de testes para cada algoritmo foi desenvolvido e é executado se você rodar o script do algoritmo em questão.
Para a criação dos testes automatizados, foi utilizado o módulo [**unittest**](https://docs.python.org/3/library/unittest.html).

Exemplo, algoritmo da Maior Subsequência Comum (LCS):
```python
import unittest
class TestLcs(unittest.TestCase):

    def test_example(self):
        self.assertEqual(lcs('ABC', 'AC', 3, 2), 2)
```

Para rodar toda a suíte de testes, use o seguinte comando no terminal no diretório raiz do projeto:

```
$ make test
```