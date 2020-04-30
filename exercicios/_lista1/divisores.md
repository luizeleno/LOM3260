---
nav_order: 5
dificuldade: 15
tags: [cond, loop]
mathjax: true
title: Divisores
---

Crie um programa que peça ao usuário um número e imprima todos os seus divisores. Se você não lembra o que é um divisor, é um número que divide outro sem deixar resto. Por exemplo, 13 é um divisor de 26 porque 26/13 não tem nenhum resto.

### Solução

```python
n = int(input('Digite um número:'))

print(f'Divisores de {n}:')
for d in range(1, n):
    if n % d == 0:
        print(d)        
```
