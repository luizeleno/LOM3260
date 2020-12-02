---
nav_order: 19
dificuldade: 40
tags: [cond, loop, string, func]
mathjax: true
title: Código César
label: cesar
---

Um dos primeiros exemplos conhecidos de criptografia foi usado por Júlio César, que precisava fornecer instruções escritas para seus generais, mas não queria que seus inimigos descobrissem seus planos se a mensagem caísse em mãos erradas. Como resultado, ele desenvolveu o que mais tarde ficou conhecido como Código de César. A ideia é simples mas, em consequência, não fornece proteção contra técnicas modernas de quebra de código. Cada letra na mensagem original é deslocada de 3 lugares. Por exemplo, A torna-se D, B torna-se E, C torna-se F, D torna-se G, etc. As últimas três letras do alfabeto são enroladas de volta do início: X torna-se A, Y torna-se B e Z torna-se C. Caracteres não alfabéticos ficam inalterados. Escreva um programa que implemente o  Código de César. Permita ao usuário fornecer a mensagem e o valor do deslocamento (não necessariamente 3) e, em seguida, exiba a mensagem codificada. Garanta que seu programa codifique letras maiúsculas e minúsculas de modo coerente. Faça com que seu programa suporte também valores de deslocamento negativos, para que possa ser usado tanto para codificar quanto para decodificar mensagens.

### Dicas

1. Os caracteres da Tabela ASCII correspondentes às letras A-Z e a-z estão, respectivamente, nas posições 65-90 e 97-122. Os algarismos de 0 a 9 correspondem às posições de 48 a 57.
1. Os seguintes comandos são úteis para esse (e outros) exercícios:
  - `ord(c)`: retorna um `int` com a posição do caractere `c` na Tabela ASCII. Por exemplo, `ord('A')` retorna `65`.
  - `chr(n)`: retorna o caractere correspondente ao inteiro `n`. Por exemplo, `chr(122)` retorna `'z'`.

<!-- more -->
  
## Solução
  
 ```python
# Entrada
mensagem = input('Digite sua mensagem:\n')
shift = int(input('shift= '))

# Algoritmo
coded = ''
for c in mensagem:
    c_ascii = ord(c)
    if c_ascii >= 65 and c_ascii <= 90:
        c_ascii += shift
        if c_ascii > 90:
            c_ascii -= 26
        elif c_ascii < 65:
            c_ascii += 26
    elif c_ascii >= 97 and c_ascii <= 122:
        c_ascii += shift
        if c_ascii > 122:
            c_ascii -= 26
        elif c_ascii < 97:
            c_ascii += 26
    coded += chr(c_ascii)

# Saída
print('Mensagem codificada:')
print(coded)
```
