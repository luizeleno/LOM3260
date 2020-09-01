---
nav_order: 1
dificuldade: 10
tags: [cond]
mathjax: true
title: Anos bissextos
label: bissexto
---

A maioria dos anos tem 365 dias. No entanto, o tempo necessário para a Terra orbitar o Sol é na verdade um pouco maior que isso. Para corrigir essa diferença, um dia extra, 29 de fevereiro, está incluído em alguns anos, ditos bissextos. As regras para determinar se um ano é ou não um ano bissexto são as seguintes:

| 1. qualquer ano que seja divisível por 400 é um ano bissexto;|
| 2. dos anos restantes, qualquer ano que seja divisível por 100 não é um ano bissexto; |
| 3. dos anos restantes, qualquer ano que seja divisível por 4 é um ano bissexto; |
| 4. todos os outros anos não são anos bissextos. |

Escreva um programa que leia um ano do usuário e exiba uma mensagem dizendo se ele é ou não um ano bissexto. Você consegue pensar num algoritmo mais eficiente, que faça em média menos testes?

### Dicas para responder à pergunta final:
- Veja que o algoritmo proposto no enunciado testa inicialmente se um número é múltiplo de 400. Apenas um em 400 números é múltiplo de 400. Portanto, 399 de 400 (99.75%) não passam no primeiro teste e vão para o segundo.
- Similarmente, um a cada 100 números é múltiplo de 100, então 99 de 100 (99%) não passam pelo segundo teste e vão para o terceiro.
- Assim, em média, o algoritmo proposto faz muito mais comparações do que o necessário. Repensando os testes a serem feitos, é possível reduzi-los em número. Por exemplo, se você começar com o teste `ano % 4 != 0`, 3 de 4 casos resultam em `True`, ou seja, esse é o único teste que você precisaria fazer em 75% dos casos.

<!-- more -->

## Solução

```python
# Entrada de dados

ano = input('Digite o ano: ')

# Código - algoritmos

ano = int(ano) # convertendo ano de string para int

if ano % 400 == 0:  # é múltiplo de 400
    resultado = True
elif ano % 100 == 0:  # é múltiplo de 100
    resultado = False
elif ano % 4 == 0:  # é múltiplo de 4
    resultado = True
else:  # não é múltiplo de 4
    resultado = False

# Saída de dados

if resultado == True:
    res = 'é'
else:
    res = 'não é'

s = f'{ano} {res} bissexto' # mensagem formatada
print(s)
```

### Análise da Solução

Dado que, de cada 400 números, 100 (25%) são divisíveis por 4, 1 (0.25%) é divisível por 400 e 3 (0.75%) são divisíveis por 100 mas não por 400, concluimos que, de todos os anos possíveis,
* 0.25%: apenas um teste (`if`) é necessário;
* 0.75%: dois testes (if e 1º `elif`) são necessários;
* 99%: três testes (24% passam no teste do 2º `elif` e 75% vão para o else) são necessários.

O número médio de testes é então

$$  N = 1 \times \frac{0.25}{100} + 2 \times \frac{0.75}{100} + 3 \times \frac{99}{100} = 2.9875  $$

Esse é um número de testes muito alto para um problema tão simples. Portanto, o algoritmo proposto no enunciado não é muito eficiente.

## Solução otimizada

Com as dicas do enunciado e usando a construção `if elif else`, a melhor solução para o problema (*melhor* no sentido estatístico, ou seja, aquela que faz, em média, menos testes) é a seguinte:
```python
if ano % 4 != 0:  # não é múltiplo de 4
    resultado = False
elif ano % 100 != 0:  # é multiplo de 4 mas não de 100
    resultado = True
elif ano % 400 != 0:  # é múltiplo de 100 mas não de 400
    resultado = False
else:  # é múltiplo de 400
    resultado = True
```

Vamos fazer a análise novamente. De todos os anos possíveis,
* 75%: apenas um teste (`if`) é necessário;
* 24% dois testes (if e 1º `elif`) são necessários;
* 1%: três testes (0.75% passam no teste do 2º `elif` e 0.25% vão para o else) são necessários.

O número médio de testes nesse caso é então

$$  N = 1 \times \frac{75}{100} + 2 \times \frac{24}{100} + 3 \times \frac{1}{100} = 1.26  $$

Uma melhora excelente! Conseguimos reduzir em quase 60% o número de comparações, reduzindo de forma parecida o tempo de execução do código. Pense no caso em que seu código precisa ser rodado bilhões ou trilhões de vezes num único dia, qual seria a economia de energia e recursos!
