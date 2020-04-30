---
title: Saída com print()
parent: temaone
nav_order: 4
status: green
tags: [input, entrada, output, saída, print, formatação, formatada, interpoladas, f-strings, substituição]
---

Como iniciantes fornecem informações ao usuário
{: .lead }

Assim como na entrada de informações, você deve estar acostumado a programas e aplicativos fornecerem informações de forma gráfica, como no exemplo do botão abaixo:

<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">
  Clique aqui!
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header text-light bg-primary">
        <h5 class="modal-title" id="exampleModalLongTitle">Informação</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        O valor de 5 ao quadrado é 25.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary text-light bg-primary" data-dismiss="modal">Fechar</button>
      </div>
    </div>
  </div>
</div>

Vamos começar de forma mais modesta e ver como fornecer informações para o usuário, que espera resultados do seu programa, na forma de uma TUI (interface de texto com o usuário), assim como fizemos para a entrada de dados.

Para imprimir qualquer informação na tela, o comando usado é o `print()`. Por exemplo,
```python
x = 5
print(x)
```

Pode-se usar o comando `print()` para imprimir vários valores:
```python
x = 5
y = x * x
print('O valor de', x, 'ao quadrado é', y)
```
que resulta na frase `O valor de 5 ao quadrado é 25` impressa na sua tela. Repare que o python adiciona um espaço em branco entre os dados impressos.

### Saída formatada

Existem diversas maneiras de **formatar** o que será impresso pelo comando `print()`. A mais indicada para iniciantes é o uso de **strings interpoladas**, ou **f-strings**, implementada a partir do Python 3.6 -- não funciona em versões anteriores do python! 

Lembre que uma string é uma sequência de caracteres: `s='x ao quadrado é igual a y'`. Mas você pode precedê-la com o caracter `f` torná-la interpolável: qualquer variável dentro de chaves (`{}`) na string será substituída pelo valor dessa variável. Por exemplo, veja o código abaixo:
```python
x = 5
y = x * x
s = f'O valor de {x} ao quadrado é {y}'
print(s)
```
O python simplesmente substitui (interpola) os valores das variáveis `x` e `y` na sua string! Depois disso, basta imprimi-la normalmente. Veja que você pode fazer tudo --- cálculo, interpolação e impressão --- numa única linha:
```python
x = 5
print(f'O valor de {x} ao quadrado é {x*x}')
```
Conveniente, não concorda?

Existem outras maneiras de gerar strings formatadas e facilitar a saída de informações para o usuário (que não veremos nesse curso). O próprio método de f-strings tem muitas opções para configurar a maneira como as variáveis são manipuladas antes de gerar a string final. Mas veremos isso mais adiante. 
