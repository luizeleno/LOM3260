---
nav_order: 21
dificuldade: 20
tags: [cond, loop, string]
mathjax: true
title: Senha aleatória
---

Escreva um programa para gerar uma senha aleatória. A senha deve ter um comprimento aleatório entre 7 e 10 caracteres (use a função `randint()` do módulo `numpy.random`). Cada caractere deve ser aleatoriamente selecionado das posições 33 a 126 na tabela ASCII. Sua função deve retornar a senha gerada aleatoriamente como único resultado, sem necessidade de entrada do usuário.
**Dica:** a função `chr()` é útil para resolver esse exercício.

<!-- more -->

### Solução

```python
import numpy.random as rd
L = rd.randint(7, 11)  # tamanho da senha
s = rd.randint(33, 127, size=L)  # senha com L caracteres no intervalo 33-126
# imprime a senha:
senha = ''
for c in s:
    senha += chr(c)
print(senha)
```

:bulb: Observação: existe uma maneira mais rápida de imprimir a senha usando o comando `join()` e *list comprehension*. Troque as últimas linhas do código acima (depois do comentário `# imprime a senha`) pelo que segue:
{: .alert .alert-success }
```python
senha = ''.join(chr(c) for c in s)
print(senha)
```


