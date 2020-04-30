---
title: Argumentos obrigatórios e opcionais
parent: temathree
nav_order: 6
status: green
mathjax: true
tags: [funções, função, def, return, argumentos, opcionais, obrigatórios, nome, pizza, tolerância, precisão, pre-definidos, padrão]
---

Funções podem ter argumentos opcionais com valores pré-definidos
{: .lead }

## Argumentos opcionais

Chegou a hora de cumprir (parcialmente) a promessa que eu fiz quando falei pela primeira vez do comando `help()` na página sobre [Documentação]({{site.baseurl}}/docs/tema3/documentacao.html). Ali vimos que a função `print()` tem uma série de argumentos opcionais, além dos obrigatórios (que são os objetos que queremos imprimir, naturalmente). Já vimos exemplos disso antes: a função `range()`, por exemplo, pode ser chamada com um argumento obrigatório (`end`) e até dois opcionais (`start` e `step`), como vimos na última aula do Tema 1, [Comandos in e len()]({{site.baseurl}}/docs/tema1/in-len.html).

Vamos lá então ver mais detalhes. Para entender o que são os argumentos opcionais, comecemos considerando a função `round()`, que faz parte do python padrão. O comando `help(round)` fornece a seguinte docstring:
```
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.
```
Da docstring da função, lemos que `round()` pode ser chamada com um ou dois argumentos e serve para arredondar um float para um dado número de casas decimais. O primeiro argumento (`number`) é o número que se deseja arredondar, e esse argumento é obrigatório. Já o segundo argumento (`ndigits`), o número de algarismos decimais, é opcional. Se não for fornecido, ele tem o valor padrão (zero), e a função retornará o `int` mais próximo de `number`. Mas, se o usuário fornecer o segundo argumento, a função `round()` retornará um `float` correspondendo a `number` arredondado com o número de casas desejado. Compare as saídas dos seguintes chamados à função `round()`:
```python
x = 3.141592653589793
print(round(x))
print(round(x, 0))
print(round(x, 1))
print(round(x, 2))
```

## Argumentos por nome

Vamos agora fazer um malabarismo. Conhecer os nomes das variáveis usadas como referência aos argumentos é uma informação interessante: Se os conhecemos, podemos chamar a função usando **named arguments**, ou *argumentos por nome*. Veja esse exemplo:
```python
x = 3.141592653589793
y = round(number=x, ndigits=2)
print(y)
```
Essa chamada a `round` é 100% equivalente a `round(x, 2)`. Mas, com argumentos por nome, podemos até mesmo trocar a ordem dos argumentos: 
```python
x = 3.141592653589793
y = round(ndigits=2, number=x)
print(y)
```
Tudo continua exatamente equivalente.

Pode parecer pouca vantagem nesse ponto, mas usar argumentos por nome é uma ótima maneira de deixar seu código mais legível, se usamos nomes auto-explicativos, além de tornar irrelevante a ordem dos argumentos nas chamadas à função. 

:warning: Se você não usa argumentos por nome, a ordem dos argumentos continua importante!!!
{: .alert .alert-warning}

Você também pode mesclar a maneira como fornece os argumentos: uma parte sem nomes, outra parte com:
```python
x = 3.141592653589793
y = round(x, ndigits=2)
print(y)
```
Esse código também é equivalente aos anteriores.

:x: Não se pode começar com argumentos por nome e depois fornecer argumentos sem nome. Por exemplo, `round(ndigits=2, 5)` termina numa mensagem de erro (faça o teste!), assim como `round(number=5, 2)`, mas `round(5, ndigits=2)` é plenamente aceitável. 
{: .alert .alert-danger }

## Crie funções com argumentos opcionais

Com os conhecimentos apenas adquiridos, podemos começar a criar nossas próprias funções com argumentos opcionais. É um processo muito simples: basta usar valores padrão quando da definição da função usando `def`. Eu sei que isso não quer dizer nada pra você! Então vamos ver um exemplo.

<div class="col-md-3 float-right">
{% include figure.html image='/assets/images/tikz/setor-circulo.png-1.png' id='circ' caption='Um setor circular' %}
</div>

Para manter as coisas simples, vamos definir uma função para calcular a área de um setor circular (uma fatia de pizza!) de ângulo $\theta$ num círculo de raio $r$, como na figura. A área em questão é dada pela fórmula a seguir: 

$$ A=\frac{1}{2} \theta r^2 $$

sendo que $\theta$ precisa estar em radianos. Além disso, a sua função deve calcular a área do círculo completo ($\theta=2\pi$) se o usuário fornecer só o raio, que é então o único argumento obrigatório.

Eu faria assim: 
```python
import numpy as np

def area_pizza(raio, theta=2*np.pi):
  return .5 * theta * raio * raio
```

Veja, em primeiro lugar, que eu importei o `numpy` para poder usar a definição de $\pi$ contida nesse módulo (`numpy.pi`). A seguir, veja que, na definição da função `area_pizza`, o argumento `raio` não tem nenhum valor pré-definido, diferente de $\theta$, cujo valor pré-definido é `2*np.pi`. Por isso:
- `raio` é um argumento obrigatório da função;
- `theta` é um argumento opcional, sendo que o valor pré-definido (padrão) é `2*np.pi`;
- os argumentos obrigatórios devem vir antes dos opcionais na definição da função usando `def`.

Assim, todo argumento opcional tem um valor pré-definido e vice-versa: todo argumento com um valor pré-definido é opcional.

Você pode deixar as coisas mais claras para o usuário se acrescentar uma docstring:
```python
import numpy as np

def area_pizza(raio, theta=2*np.pi):
  '''
    Calcula a área de uma fatia de pizza 
    
    Uso: 
      area_pizza(raio, theta=2*np.pi)
    
    entrada:
      - raio (float, obrigatório): o raio da pizza
      - theta (float, opcional, padrão: 2*pi): o ângulo da fatia.
          Se não for fornecido, calcula a área da pizza inteira.
    saída:
      - a área da fatia (float)
  '''
  return .5 * theta * raio * raio
```

Vamos então brincar com a função com algumas chamadas. Teste todas no intérprete python!
```python
import numpy as np

r = 25  # pizza com diâmetro de 50cm!
corte = 2 * np.pi / 8  # um de oito pedaços da pizza

Apizza = area_pizza(r)
Apedaco = area_pizza(r, corte)
Apedacoduplo = area_pizza(r, 2*corte)
```

Vamos agora calcular a área de um pedaço de pizza chamando a função de várias maneiras equivalentes:
```python
import numpy as np

r = 25  # pizza com diâmetro de 50cm!
corte = 2 * np.pi / 8  # um de oito pedaços da pizza

# todos os chamados à função abaixo são equivalentes:
Apedaco = area_pizza(r, corte)
Apedaco = area_pizza(raio=r, theta=corte)
Apedaco = area_pizza(theta=corte, raio=r)
Apedaco = area_pizza(r, theta=corte)
```

Valores pré-definidos são uma excelente opção para funções mais complexas, permitindo ao usuário utilizar rapidamente suas funções confiando que você escolheu valores sensatos para os argumentos opcionais!

Por exemplo, argumentos como precisão, tolerância, método de cálculo e número máximo de iterações de um procedimento numérico podem ter valores pré-definidos que sejam razoáveis para a maior parte das situações práticas. Caso o usuário deseje ou precise, ele pode alterar os argumentos opcionais por sua própria conta. Essa maneira de trabalhar será muito importante quando começarmos a ver os métodos do cálculo numérico.
