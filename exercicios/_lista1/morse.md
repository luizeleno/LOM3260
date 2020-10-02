---
nav_order: 27
dificuldade: 25
tags: [loop, string, dict]
mathjax: true
title: Código Morse
label: morse
---

O **código Morse** é um esquema de codificação que usa traços e pontos para representar números e letras. Neste exercício, você vai escrever um programa que usa um dicionário para armazenar o mapeamento de letras e números para código Morse, mostrado na tabela a seguir:

|	A | . -     | J | . - - - | S | . . .     | 1 | . - - - - |
|	B | - . . . | K | - . -   | T | -         | 2 | . . - - - |
|	C | - . - . | L | . - . . | U | . . -     | 3 | . . . - - |
|	D | - . .   | M | - -     | V | . . . -   | 4 | . . . . - |
|	E | .       | N | - .     | W | . - -     | 5 | . . . . . |
|	F | . . - . | O | - - -   | X | - . . -   | 6 | - . . . . |
|	G | - - .   | P | .- -.   | Y | - . - -   | 7 | - - . . . |
|	H | . . . . | Q | - -.-   | Z | - - . .   | 8 | - - - . . |
|	I | . .     | R | . - .   | 0 | - - - - - | 9 | - - - - . |


Seu programa deve ler uma mensagem do usuário. Então deve traduzir cada
letra e número na mensagem para o código Morse, deixando um espaço entre cada
seqüência de traços e pontos. Seu programa deve ignorar quaisquer caracteres que não sejam letras ou números. O código Morse para `Hello, World!` é mostrado abaixo:
```
....  .  .-..  .-..  ---   .--  ---  .-.  .-..  -..
```

<!-- more -->

A solução abaixo usa um dicionário e uma função para converter minúsculas em maiúsculas e eliminar caracteres não alfanuméricos

```python
morse = {'A':	'.-',	'J':	'.---',	'S':	'...',	'1':	'.----',
'B':	'-...',	'K':	'-.-',	'T':	'-'	,	'2':	'..---',
'C':	'-.-.',	'L':	'.-..',	'U':	'..-',	'3':	'...--',
'D':	'-..',	'M':	'--',	'V':	'...-',	'4':	'....-',
'E':	'.',		'N':	'-.',	'W':	'.--',	'5':	'.....',
'F':	'..-.',	'O':	'---',	'X':	'-..-',	'6':	'-....',
'G':	'--.',	'P':	'.--.',	'Y':	'-.--',	'7':	'--...',
'H':	'....',	'Q':	'--.-',	'Z':	'--..',	'8':	'---..',
'I':	'..',	'R':	'.-.',	'0':	'-----',	'9':	'----.'}

def converte(msg):
  '''
    converte minúsculas e maiúsculas e
    elimina caracteres não alfanumericos
  '''
  msg1 = ''
  for c in msg:
    if 'a' <= c <= 'z':
      msg1 += chr(ord(c)-32)
    elif 'A' <= c <= 'Z' or '0' <= c <= '9':
      msg1 += c

  return msg1

mensagem = input('Digite sua mensagem: ')
mensagem = converte(mensagem)
for c in mensagem:
  print(morse[c], end=' ')
print()

  ```
