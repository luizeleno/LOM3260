---
nav_order: 18
dificuldade: 35
tags: [cond, loop, dict]
mathjax: true
title: Dia seguinte
label: diaseguinte
---

Escreva um programa que leia uma data do usuário e calcule o dia seguinte. Por exemplo, se o usuário inserir valores que representem 18/11/2013, o programa deve exibir 19/11/2013. A data deve ser inserida em formato numérico com três declarações de entrada separadas, uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa funcione corretamente para anos bissextos.

<!-- more -->

## Solução

Segue uma solução usando dicionários e uma função para determinar se um ano é bissexto:

```python
def fevereiro(ano):
    # retorna o no. de dias em fevereiro do ano
    return 29 if (not ano % 4 and ano % 100) or not ano % 400 else 28

# entrada de dados
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))
print(f'dia atual: {d:02d}/{m:02d}/{a}')

# durações de todos os meses
duracoes = {1: 31, 2: fevereiro(a), 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if d < duracoes[m]:  # não é o último dia do mês
    d += 1  # apenas incrementa o dia
elif m == 12:  # último dia do mês 12
    d = 1  # incrementa o ano
    m = 1
    a += 1
else:  # último dia dos meses 1-11
    d = 1  # incrementa o mês
    m += 1

# imprimindo o resultado
print(f'dia seguinte: {d:02d}/{m:02d}/{a}')
```
