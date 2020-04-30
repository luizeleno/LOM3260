---
nav_order: 12
dificuldade: 15
tags: [string, loop]
mathjax: true
title: Números binários I
---

Escreva um programa que converta um número binário (base 2) em decimal (base 10). Seu programa deve ler o número binário do usuário como uma sequência de zeros e uns e exibir o número decimal equivalente, processando cada dígito da representação binária. Por exemplo, 1010011 (base 2) $\equiv$ 83 (base 10), obtido a partir da definição:

$$
1010011 \text{ (base 2)} =
$$

$$
= \mathbf{1} \times 2^6 +
\mathbf{0} \times 2^5 +
\mathbf{1} \times 2^4 +
$$

$$
+ \mathbf{0} \times 2^3 +
\mathbf{0} \times 2^2 +
\mathbf{1} \times 2^1 +
\mathbf{1} \times 2^0 =
$$

$$
= 83 \text{ (base 10)}
$$


### Solução

```python
# Input
binario = input('Digite um número em base 2: ')

# Algoritmo

soma = 0
p = 1  # = 2**expoente

for digito in binario[::-1]:  # slicing para inverter a string
    soma = soma + int(digito) * p
    p = 2 * p

# Output
print(f'{binario} (base 10) = {soma} (base 2)')

```
