---
nav_order: 1
dificuldade: 10
tags: [cond]
mathjax: true
title: Anos bissextos
---

A maioria dos anos tem 365 dias. No entanto, o tempo necessário para a Terra orbitar o Sol é na verdade um pouco maior que isso. Para corrigir essa diferença, um dia extra, 29 de fevereiro, está incluído em alguns anos, ditos bissextos. As regras para determinar se um ano é ou não um ano bissexto são as seguintes:

| 1. qualquer ano que seja divisível por 400 é um ano bissexto;|
| 2. dos anos restantes, qualquer ano que seja divisível por 100 não é um ano bissexto; |
| 3. dos anos restantes, qualquer ano que seja divisível por 4 é um ano bissexto; |
| 4. todos os outros anos não são anos bissextos. |
    
Escreva um programa que leia um ano do usuário e exiba uma mensagem dizendo se ele é ou não um ano bissexto. Você consegue pensar num algoritmo mais eficiente, que faça em média menos testes?

### Solução

```python
# Entrada de dados

ano = input('Digite o ano: ')

# Código - algoritmos

ano = int(ano) # convertendo ano de string para int

if ano % 400 == 0:  # resto da divisão de ano por 400
    resultado = True
elif ano % 100 == 0:
    resultado = False
elif ano % 4 == 0:
    resultado = True
else:
    resultado = False

# Saída de dados

if resultado == True:
    res = 'é'
else:
    res = 'não é'

s = f'{ano} {res} bissexto' # mensagem formatada
print(s)
```

### Dicas para responder à pergunta final:
- Veja que o algoritmo proposto no enunciado testa inicialmente se um número é múltiplo de 400. Apenas um em 400 números é múltiplo de 400. Portanto, 399 de 400 (99.75%) casos vão para o primeiro elif.
- Similarmente, um a cada 100 números é múltiplo de 100, então 99 de 100 (99%) casos vão para o segundo elif.
- Assim, em média, o algoritmo proposto faz muito mais comparações do que o necessário. Rearranjando a ordem dos testes, é possível reduzir o número de testes. Por exemplo, se você começar com o teste ano % 4 != 0, 3 de 4 casos resultam em True, ou seja, esse é o único teste que você precisaria fazer para 75% dos casos.
