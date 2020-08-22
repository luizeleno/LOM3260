---
title: Módulos
parent: temathree
nav_order: 1
status: green
tags: [funções, função, módulo, module, numpy, from, as, apelido, import, raiz, sqrt, padrão, standard]
timestamp: 22/08/20
---

Existem muitos módulos em python especializados numa imensa gama de tarefas!
{: .lead }

## A Biblioteca Padrão de Python

A linguagem python tem por padrão várias funções, suficientes para criar programas bastante complexos. A lista abaixo fornece praticamente todas as palavras-chaves do python padrão (*Standard Python*):

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

Outras palavras, como `int`, `float`, `print`, `input`, etc.,  estão reservadas para funções, tipos de dados, operadores, etc. Consulte a documentação sobre a **[Biblioteca Padrão de Python](https://docs.python.org/3/library/){: target="\_blank"}** (*Python Standard Library*) para uma lista gigante e praticamente completa.

## Módulos

Mesmo com todos esses recursos, o python só se tornou a mais importante ferramente computacional da atualidade pela sua capacidade de extender seus poderes usando **módulos,** que são conjuntos (ou bibliotecas) de novos tipos de dados, métodos, operadores e funções  criados com uma finalidade específica em mente: lidar com arquivos, resolver problemas numéricos, inteligência artificial, etc, etc, etc.

A lista de módulos disponíveis é praticamente infinita, impossível de ser listada aqui. Como o curso pretende lidar com técnicas computacionais de análise numérica de dados, vamos focar num subconjunto pequeno dos módulos python para essa finalidade. Anida assim, mesmo sem conseguir trabalhar aqui com mais do que um pequeno punhado de módulos, começaremos com comandos básicos, válidos para qualquer um deles. Com isso, você pode procurar nos [Recursos]({{site.baseurl}}/biblio/) outros módulos que lhe interessem e testá-los para seus objetivos. Veremos também, mais adiante, como criar nosso próprio módulo personalizado!

Para fixar as ideias, vamos usar como exemplo o módulo chamado `numpy`. Você pode extrapolar os conceitos e comandos mostrados abaixo para qualquer módulo.

:warning: O módulo `math` tem algumas funções parecidas com as encontradas no `numpy`. No entanto, o `math` não é atualmente recomendável para computação científica. Evite usá-lo!
{: .alert .alert-warning }

Usaremos como motivação o seguinte problema: digamos que você precise calcular a raiz quadrada de um número. O python padrão não tem uma função para isso, mas pode ser adicionada se você incluir no seu código algum módulo que contenha essa função. O módulo `numpy` é o mais indicado: ele contém muitas funções matemáticas, como seno, cosseno, exponential, raiz quadrada, etc.

:bulb: Um dos exercícios da Lista 1 ([esse aqui]({{site.baseurl}}/material/exercicios/lista1.html#ex20)) ilustra uma possível maneira de calcular a raiz quadrada sem usar um módulo externo, usando uma estratégia numérica conhecida por *Método de Newton-Raphson*. Você poderia usá-la em seus próprios módulos personalizados...
{: .alert .alert-primary }

## Importanto módulos

Vejamos, então, como incluir um módulo externo no código. Isse é feito com o comando `import`. De forma direta, basta incluir a seguinte linha no começo do seu programa:
```python
import numpy
```
Com isso, importamos **todas** as funções e métodos disponibilizados pelo módulo numpy. Por exemplo, a função raiz quadrada é chamada de `sqrt` (do inglês *square root*). Usando `import numpy`, a função ficará acessível ao seu programa como `numpy.sqrt`. Você então a chamaria assim:
```python
import numpy

a = 5.0
rqa = numpy.sqrt(a)

print(f'A raiz quadrada de {a} é {rqa}')
```

Essa, no entanto, é apenas uma das maneiras de usar o comando `import`. Uma outra maneira é dar um "apelido" ao módulo com a palavra chave `as` (*como*):
```python
import numpy as np
```
onde `np` é o apelido escolhido (é da escolha do programador). Nesse caso, acessamos a função `sqrt` precedida pelo apelido, `np.sqrt`, e não mais pelo nome (`numpy.sqrt`). Veja a diferença:
```python
import numpy as np

a = 5.0
rqa = np.sqrt(a)

print(f'A raiz quadrada de {a} é {rqa}')
```

Uma terceira maneira de usar o import é a seguinte, usando o método `from` (*de*):
```python
from numpy import *

a = 5.0
rqa = sqrt(a)

print(f'A raiz quadrada de {a} é {rqa}')
```
A linha `from numpy import *` diz, literalmente (em inglês), *de numpy importe tudo*. O caractere `*` (asterisco) é chamado de **caractere-coringa** (*wildcard*, em inglês) pois, em analogia a jogos de cartas, ele tem o valor que você quiser, ou tudo ao mesmo tempo. Repare que, usando essa maneira de importar, as funções são usadas sem nenhuma qualificação de origem, ou seja, usamos diretamente `sqrt(a)`, e não `numpy.sqrt(a)` ou `np.sqrt(a)`. Com a construção `from import`, você poderia também importar apenas a função que lhe interessa:
```python
from numpy import sqrt

a = 5.0
rqa = sqrt(a)

print(f'A raiz quadrada de {a} é {rqa}')
```
Isso tem um certo ganho de eficiência, pois menos funções, métodos e variáveis são criadas pelo seu programa, usando assim menos memória. Mas essa vantagem é contrabalanceada pelo seguinte problema:

:x: Fuja do uso da construção `from modulo import *` ou `from modulo import metodo`. Isso não é recomendado, pois seu programa poderia ter funções ou variáveis com o mesmo nome de funções ou variáveis do `modulo` importado. Esses *conflitos* levariam a erros de execução.
{: .alert .alert-danger }

Para evitar isso, você pode combinar a construção `from` com `as`, importando apenas a função `sqrt` do `numpy`, mas dando-lhe um apelido:

```python
from numpy import sqrt as raiz

a = 5.0
rqa = raiz(a)

print(f'A raiz quadrada de {a} é {rqa}')
```

É pouco provável que exista uma função `raiz` no numpy, então o problema é contornado --- mas sem nenhuma garantia: e se um dos desenvolvedores do `numpy` é lusófono e usou a palavra `raiz` internamente no código? Por isso, eu não recomendo usar a construção `from`, nem mesmo com o uso concomitante do `as`. É melhor, por segurança e compatibilidade, importar os módulos completos, com `import numpy` ou `import numpy as np`.
