---
nav_order: 13
dificuldade: 15
tags: [loop]
mathjax: true
title: Números binários II
---

Escreva um programa que converta um número decimal (base 10) em binário (base 2). Leia o número decimal do usuário e use o seguinte algoritmo de divisão, exemplificado para o número 83 (base 10):
```
	83/2 = 41 resto 1
	41/2 = 20 resto 1
	20/2 = 10 resto 0
	10/2 = 5 resto 0
	5/2 = 2 resto 1
	2/2 = 1 resto 0
	1/2 = 0 resto 1
```
Os restos das divisões (começando do último valor) contém a representação binária do número, nesse caso 1010011 (base 2).

<!-- more -->

### Solução
```python
# Entrada

decimal = int(input('N (base 10) = '))

# Algoritmo

# inicialização das variáveis
quociente = decimal
binario = ''

'''
comentários:
- quociente vair receber, a cada iteração, o resultado da divisão por 2
- binário é uma string inicialmente vazia, que receberá os restos das divisões por dois
- usamos o operador concatenação de strings (+) para construir a representação binária
'''

while quociente > 0:
    resto = quociente % 2
    quociente = quociente // 2
    binario = str(resto) + binario

# Saída
print(f'{decimal} (base 10) = {binario} (base 2)')

```


