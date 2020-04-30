---
title: Números aleatórios
parent: temafour
status: red
tags: [numpy, scipy, arrays]
---

Gerar números aleatórios é uma das tarefas mais importantes da computação científica
{: .lead}

## Aleatoriedade em computação

Como exemplo de módulos da família `numpy/scipy`, vejamos um que fornece recursos importantíssimos para a computação científica. Gerar dados aleatórios  é fundamental para o teste de hipóteses e modelos e estão na base de modelos físico-estatísticos como o Método de Monte Carlo, usualmente encontrado em disciplinas como *Métodos computacionais da Física* (aqui na EEL, [LOM3227](https://uspdigital.usp.br/jupiterweb/jupDisciplina?sgldis=LOM3227&verdis=1){: target="\_blank"}) ou outras correlatas. Antigamente (bem antigamente mesmo, antes da era digital!), qualquer livro de Probabilidades e Estatística contava com um apêndice contendo uma tabela de números aleatórios. Podemos apenas imaginar como tais tabelas eram geradas: usando dados e moedas?

Hoje em dia, porém (na verdade, desde a década de 1940!), a computação para a geração de números aleatórios está muito mais avançada e qualquer computador é capaz de gerar séries enormes de dados aleatórios. 

A verdade, porém, é mais complexa. Um computador é uma máquina praticamente determinística, e não consegue (ou tem grandes dificuldades) em criar informações que sejam, de fato, aleatórias. Existem, na verdade, geradores de números pseudo-aleatórios, ou seja, que apenas parecem aleatórios. Veremos mais detalhes sobre isso  na disciplina mencionada anteriormente. Por enquanto, vamos nos concentrar apenas em como usar o módulo `numpy.random` para gerar sequências de valores `int` e `float` que são, para todos os efeitos, aleatórias.

## O módulo `numpy.random`

Em inglês *random* significa *aleatório*.   

```
import numpy.random as rd
```
