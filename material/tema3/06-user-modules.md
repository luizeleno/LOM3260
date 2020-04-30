---
title: Módulos do usuário
parent: temathree
nav_order: 5
status: green
tags: [funções, função, def, return, docstring, módulo, personalizado, main]
---

Você pode agrupar suas funções e criar seus próprios módulos!
{: .lead }

## O módulo `__main__`

Voltemos por um momento a uma função simples, aquela que calcula o quadrado de um número, que vimos nas duas últimas lições:
```python
def quadrado(x):
  '''
    Retorna o quadrado de um número
    - Input:
      - x: um int ou float
    - Output: x*x (que é o mesmo que x ao quadrado) 
  '''
  return x * x
```
Use agora `help(quadrado)`. O resultado é, como esperávamos, nosso docstring:
```
Help on function quadrado in module __main__:

quadrado(x)
    Retorna o quadrado de um número
    - Input:
      - x: um int ou float
    - Output: x*x (que é o mesmo que x ao quadrado)
```
Mas repare na primeira linha impressa pelo `help()`: *Help on function quadrado in module __main__*. Essa mensagem nos diz que a função `quadrado()` faz parte de um módulo chamado `__main__`. *Main* ("principal") é o nome (*name*) do arquivo que você "roda" com o python. Você pode dar qualquer título para seu arquivo (por exemplo, `meu_arquivo.py`) e rodá-lo em python. Seja qual for o título do arquivo, o python vai considerá-lo como um módulo (`module`) com o nome `__main__`. Em outras palavras, você já vem trabalhando com módulos desde o seu primeiro contato com python! 

# Criando um módulo

Qualquer outro arquivo incluído com `import` no arquivo `__main__` é um outro módulo. Você pode, portanto, criar um arquivo, digamos, `meu_modulo.py`, colocar lá a sua função (quantas funções você quiser, na verdade), e importá-lo no arquivo principal.

:warning: Seus módulos só vão ser visíveis a seus arquivos `__main__` se estiverem na mesma pasta no computador que o arquivo principal. Existem maneiras de "instalar" seus módulos em locais específicos do computador (que não veremos aqui :cry:), de modo a ficarem acessíveis com o comando `import` para arquivos principais guardados em qualquer pasta.
{: .alert .alert-warning }

:x: O título (nome do arquivo) de um módulo não pode conter caracteres especiais em python: acentos, hífens, espaços, e quase todos os demais caracteres não-alfanuméricos -- o *underline* (`_`) é permitido.
{: .alert .alert-danger }

Vamos fazer um exemplo passo a passo para a criação e uso de um módulo com a função `quadrado()`.

- Crie um arquivo chame-o de `meu_modulo.py` com o seguinte conteúdo:
      
```python
'''
modulo meu_modulo

Um módulo para calcular algumas propriedades numéricas

Criado por L.T.F.E. em 11/09/2019 (que medo!).
'''

def quadrado(x):
  '''
    Retorna o quadrado de um número
    - Input:
      - x: um int ou float
    - Output: x * x (que é o mesmo que x ao quadrado) 
  '''
  return x * x
```      
- No seu arquivo principal (chame-o do que quiser, por exemplo, `meu_main.py`), importe o módulo com o comando `import` da maneira que achar melhor, por exemplo, usando um apelido com `as`:

```python
import meu_modulo as mm
```
- No arquivo principal, você usa as funções do seu módulo de maneira usual, como aprendemos na lição sobre módulos. Por exemplo:

```python
import meu_modulo as mm

z = 5
y = mm.quadrado(z)
print(f'{z}² = {y}')
```

Com isso, deixamos nosso código *modularizado*, ou seja, compartimentado em unidades menores (os módulos) que são "gerenciados" por um arquivo principal (o de nome `__main__`) que comanda a execução do programa.

:+1: Quando seus programas começarem a ficar grandes, como dezenas ou mesmo centenas de linhas, a vantagem de subdividi-lo em vários arquivos (módulos) vai começar a ficar evidente!
{: .alert .alert-primary }

## Docstrings em módulos

Repare que você pode acrescentar uma docstring no seu módulo, como eu fiz no exemplo acima. Isso é extremamente útil para usuários do seu módulo que queiram saber mais informações sobre os recursos e as aplicações que ele tem para oferecer.
