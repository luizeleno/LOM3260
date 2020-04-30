---
title: Funções
parent: temathree
nav_order: 3
status: green
mathjax: true
tags: [funções, função, def, return, modular, chamar, ferramenta, argumento]
permalink: /tema3/funcoes/
---

Definir suas próprias funções -- novas ferramentas! -- torna seu código mais robusto e fácil de entender. 
{: .lead }

Aprender a criar e usar funções personalizadas é o passo mais importante para sair do nível novato e alcançar o patamar avançado. A maior parte dos usuários de python não chega a esse nível, a não ser que já tenha trabalhado com, e conheça um pouco mais a fundo, alguma outra linguagem de programação.

Os iniciantes têm certa dificuldade em entender logo de cara um código que contém a definição de uma função. Eu não sei muito bem por que isso acontece (provavelmente passei pelo mesmo problema quando estava aprendendo a programar em C, nos idos de 1995, mas já não me lembro...), mas uma **função** é uma daquelas ideias fáceis de entender... depois que você a entendeu (!), e depois você se pergunta por que teve tanta dificuldade pra entender um conceito tão simples.

Acho mais fácil começar por um exemplo. Digamos que precisamos determinar a área $A$ de um círculo, segundo a fórmula usual $A = \pi r^2$, sendo $r$ o raio do círculo em questão, que deve ser fornecido pelo usuário. Nada mais fácil:
```python
r = float(input('Digite r em centímetros:'))
pi = 3.14159  # uma aproximação para pi
A = pi * r * r
print(f'A área do círculo de raio {r} cm é A = {A} cm²')
```

Mas poderíamos também criar uma *função* e usá-la no código, para deixá-lo mais *modular*. Uma função é criada usando o comando `def` como no exemplo abaixo:
```python
def area_circulo(raio):
  pi = 3.14159
  area = pi * raio * raio
  return area
```
Veja que o nome da função (que você escolhe!), nesse caso, é `area_circulo`. A função pede um **argumento**, nesse caso, `raio` (um nome que também é de sua escolha). Dentro da função, as variáveis `pi` e `area` são definidas. Por fim, o valor da variável `area` é **retornado** ao usuário (usando `return`). 

Vejamos um exemplo da utilização dessa função:
```python
def area_circulo(raio):
  pi = 3.14159
  area = pi * raio * raio
  return area

r = float(input('Digite r em centímetros:'))
pi = 3.14159  # uma aproximação para pi
A = area_circulo(r)
print(f'A área do círculo de raio {r} cm é A = {A} cm²')
```

:bangbang: O que eu percebo, da minha experiência ensinando programação, é que muitos iniciantes empacam nesse ponto, por isso, preste atenção, pois não é difícil (depois que você entendeu :confounded:): 
{: .alert .alert-primary }
- No início do código acima, está  a **definição da função.** O python encontra o comando `def` e guarda no nome `area_circulo` as **instruções** contidas nas linhas seguintes (ou seja, nas linhas "dentro" do `def`). Mas ele não as executa! Você apenas ensinou ao python uma nova **ferramenta:** uma **função**, chamada `area_circulo`
- O python também sabe que a nova função depende de um argumento, que você decidiu chamar, *para fins da definição da função*, de `raio`.
- Depois da definição da função, ela estará disponível ao programa, e você pode **chamar** a função fornecendo-lhe o argumento que você quiser! Foi o que fizemos ao usar a função com o argumento `r` na linha `A = area_circulo(r)`.

## Funções de vários argumentos

Uma função pode ter vários argumentos. Por exemplo, para calcular a área de um retângulo, poderíamos definir a seguinte função:
```python
def area_retangulo(base, altura):
  area = base * altura
  return area
```
e um exemplo de sua utilização é o seguinte:
```python
x, y = 5, 3
A = area_retangulo(x, y)
```

## Retornando vários valores

Uma função pode também retornar mais de um valor! Por exemplo, a função abaixo retorna a área e o perímetro de um retângulo:
```python
def AP_retangulo(base, altura):
  area = base * altura
  perimetro = 2 * (base + altura)
  return area, perimetro
```
e com isso poderíamos obter as duas grandezas de uma só tacada:
```python
x, y = 5, 3
A, P = AP_retangulo(x, y)
```

## Funções podem chamar outras funções!

No último exemplo, poderíamos fazer o seguinte: definir três funções -- uma para a área, outra para o perímetro, e a última que chama as duas primeiras:
```python
def area_retangulo(base, altura):
  area = base * altura
  return area


def perimetro_retangulo(base, altura):
  perimetro = 2 * (base + altura)
  return perimetro


def AP_retangulo(base, altura):
  area = area_retangulo(base, altura)
  perimetro = perimetro_retangulo(base, altura)
  return area, perimetro
```

Assim, ganhamos flexibilidade quando queremos, por exemplo, só a área:
```python
x, y = 5, 2
A1 = area_retangulo(x, y)

a, b = 7., 6.5
A2, P2 = AP_retangulo(a, b)
```

## Sobre o comando `return`

Veja que o return pode também retornar expressões *"on the fly"* (de passagem):
```python
def quadrado(x):
  return x * x
```
Ou seja, não é imprescindível retornar um valor previamente atribuído a uma variável.
Você poderia usá-la (assim como as funções anteriores!), por exemplo, assim:
```python
c = 2.5
print(f'{c}² = {quadrado(c)}')
```
