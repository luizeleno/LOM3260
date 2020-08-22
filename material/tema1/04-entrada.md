---
title: Entrada com input()
parent: temaone
nav_order: 4
status: green
tags: [input, entrada, output, saída, print, formatação, formatada, TUI]
timestamp: 07/06/20
---

Como iniciantes interagem com o usuário
{: .lead }

Como fazer com que seu código peça informações ao usuário? Em sites e aplicativos, geralmente você fornece informações interagindo com alguma forma de interface gráfica, como os campos de texto, a caixa de verificação e o botão abaixo:

<form class="alert alert-warning">
  <div class="form-group">
    <label for="exampleInputEmail1">E-mail</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Digite seu e-mail">
    <small id="emailHelp" class="form-text text-muted">Nunca divulgaremos seu e-mail para terceiros.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Senha</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Senha">
  </div>
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Li e estou de acordo com as condições de uso</label>
  </div>
  <button type="submit" class="btn btn-primary m-1">Enviar</button>
  <small  class="form-text text-muted">(este botão não faz nada, serve apenas como ilustração).</small>
</form>

É possível criar interfaces assim em python! Infelizmente, não temos tempo de chegar a esse nível de sofisticação. Tentei fazer isso na primeira edição do curso, mas o nível de conhecimento exigido é alto demais para chegar nesse ponto em apenas um semestre! <!-- Por isso, neste curso, veremos apenas interfaces gráficas simplificadas usando o módulo `matplotlib.widgets`, bem mais adiante no curso. -->

Ainda assim, é possível desde já criar uma interface com o usuário, ainda que simples, chamada **TUI** (*text-based user interface*, ou interface de texto com o usuário). Ela é feita basicamente usando o comando `input()`. Veja o exemplo abaixo:
```python
x = input('Digite um número: ')
```
O que esse código faz é pedir um número ao usuário, que recebe como instrução a mensagem `Digite um número: `. O usuário digita o número que ele quiser e, assim que pressionar Enter, o python recebe a informação **na forma de uma string** e a atribui à variável `x`.

:warning: Em Python 3, a informação recebida do usuário pelo comando `input` é sempre do tipo `string`. Esse comportamento é diferente em versões anteriores do python!
{: .alert .alert-warning}

Se você quiser que o python interprete a informação recebida como uma variável numérica, é preciso convertê-la para o tipo desejado usando, por exemplo, `int()` ou `float()`:
```python
x = int(input('Digite um número: '))
```
Para mais clareza, você poderia separar o comando acima em duas linhas:
```python
x = input('Digite um número: ')
x = int(x)
```

Além disso, veja que o python não faz automaticamente nenhum teste para ver se o que o usuário digitou é realmente um número. Se o usuário digitar, por exemplo, `três` (e não `3`), a conversão para int não vai funcionar! Existem maneiras de verificar se o que o usuário digitou faz sentido no seu programa (a construção usada para isso é a `try` - `except`). Neste curso, no entanto, nos exemplos e exercícios, sempre imaginaremos um "usuário perfeito", que não comete erros e fornece sempre valores coerentes...
