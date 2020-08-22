---
title: Mais sobre o return
parent: temathree
nav_order: 4
status: green
mathjax: true
tags: [funções, função, def, return, chamar, ferramenta]
permalink: /tema3/return/
timestamp: 22/08/20
---

O `return` da sua função tem algumas propriedades que o ajudam a escrever seu código
{: .lead }

O primeiro exercício da Lista 1 pedia para você determinar se um dado ano é ou não bissexto. À epoca, não usamos uma função e programamos o código diretamente, seguindo o algoritmo proposto no [enunciado do exercício]({{site.baseurl}}/material/exercicios/lista1.html#ex1). No entanto, podemos criar uma função para fazer isso:
```python
def bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False
```

Não se confunda com tantos `return`! A execução da função termina assim que um comando `return` é atingido. Em outras palavras, na função acima, assim que é executado qualquer um dos comandos `return`, a função termina e você tem imediatamente o resultado. Essa é uma característica importante do comando `return`. Isso facilita, e muito, a criação, entendimento e uso de funções em python!

:bulb: Veja que a função acima não está otimizada com as dicas do exercício! Para treinar lógica de programação, recomendo que você leia as dicas encontradas no [enunciado do exercício]({{site.baseurl}}/material/exercicios/lista1.html#ex1) e adapte a função seguindo as recomendações lá encontradas.
{: .alert .alert-primary }

Repare que, para a solução do exercício sobre [senha forte]({{site.baseurl}}/material/exercicios/lista1.html#ex22), podemos usar esse conceito e criar uma função para gerar possíveis senhas e outra para testá-las.
