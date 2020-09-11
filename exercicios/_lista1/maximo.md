---
nav_order: 26
dificuldade: 20
tags: [cond, loop, list, func]
mathjax: true
title: Máximo de uma lista
label: max
---

Considere o problema de identificar o máximo valor de uma coleção de inteiros,  todos selecionados aleatoriamente no intervalo $[1,\,100]$. A coleção pode conter valores duplicados, e alguns dos números entre 1 e 100 podem não estar presentes. Pare um pouco e pense em como você lidaria com esse problema no papel. A maioria checaria cada número em sequência e perguntaria se o valor da vez é maior que o máximo dentre os anteriores. Se for, eles esqueceriam o máximo anterior e lembrariam o número atual como o novo máximo. Essa é uma abordagem razoável e resultará na resposta correta quando o processo for executado com cuidado. Implemente o método em python. Quantas vezes você esperaria precisar atualizar o valor máximo e lembrar de um novo número?

<!-- more -->

### Solução

```python
import numpy.random as rd
# exemplificando para 20 valores
L = rd.randint(1, 101, size=20)
max = L[0]
for v in L[1:]:
    if v > max:
        max = v

print(f'Na lista {L}')
print(f'o valor máximo é {max}')
```
