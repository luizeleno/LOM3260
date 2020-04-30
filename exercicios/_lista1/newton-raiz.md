---
nav_order: 20
dificuldade: 20
tags: [cond, loop]
mathjax: true
title: Raiz quadrada (Newton)
---

Escreva um programa que implementa o método de Newton para extrair a raiz quadrada de um número digitado pelo usuário. O algoritmo é o seguinte:

| 1. leia `x` do usuário; |
| 2. inicialize `raiz` em `x / 2`; |
| 3. enquanto `raiz` não for "bom o suficiente," atualize `raiz` para a média de `raiz` e `x / raiz`. |

Quando o algoritmo é concluído, `raiz` contém uma aproximação da raiz quadrada de `x`. A qualidade da aproximação depende de como você define "bom o suficiente," então adote o seguinte critério de parada: o valor absoluto da diferença entre `raiz * raiz` e `x` deve ser menor que $10^{-12}$.

### Solução

```python
'''
cálculo da raiz quadrada aproximada
usando método de Newton
com uma precisão de 1e-12
'''

x = float(input('Digite um número: '))

# Algoritmo: método de Newton para raiz quadrada
raiz = x / 2 # inicializar o palpite para a a raiz em x / 2
tolerancia = 1.e-12 # notacão científica: 1e-12 é igual a 1 * 10**(-12)
while abs(raiz**2 - x) >= tolerancia: # a função abs() retorna o módulo (valor absoluto) do seu argumento
    raiz = (raiz + x / raiz) / 2 # atualiza o valor do palpite para a raiz

print(f'A raiz quadrada de {x} é {raiz}')
```
