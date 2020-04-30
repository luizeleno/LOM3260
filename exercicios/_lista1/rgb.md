---
nav_order: 14
dificuldade: 30
tags: [loop, string, dict]
mathjax: true
title: Sistema RGB
---

Uma das maneiras de se referir a cores em *websites* e outras aplicações é a **notação RGB** (*red-green-blue*): três inteiros $0 \le R,\,G,\,B \le 255$ como identificadores das tonalidades de vermelho, verde e azul, respectivamente, que, quando mescladas, fornecem a cor desejada. Ao invés de fornecer os três inteiros em base 10, no entanto, é comum usar base 16. Essa maneira de identificar cores  é conhecida como **código hexadecimal**. Em base 16, precisamos de 16 caracteres para representar os "dígitos" de um número (veja que em base 2 precisamos de dois, e em base 10, de dez). Usualmente são escolhidos os caracteres 0--9, com os valores usuais, e portanto precisamos de mais seis caracteres para representar os "dígitos" de de 10 a 15. Usualmente usa-se as letras A--F. Por exemplo,

$$ \small
42 \text{ (base 10)} = 2A \text{ (base 16)} = 
$$

$$
= 2 \times 16^1 + 10 \times 16^0 \,.
$$

Números que em base 16 são formados por apenas dois caracteres equivalem aos números de 0 a 255 ($= 16 ^ 2 -1$) em base 10.
Além disso, no código hexadecimal as três tonalidades são indicadas por uma única *string* de seis caracteres. Por exemplo, o código hexadecimal `CD1F41` corresponde aos tons $R=205$, $G=31$ e $B=65$, como você pode conferir [aqui](https://htmlcolorcodes.com/){: target="blank"}.
Esse sistema (ou seja, seis caracteres escolhidos do conjunto 0--9+A--F) é capaz de descrever $256^3=16\,777\,216$ cores diferentes, de 000000 (preto) a FFFFFF (branco). Com base nos exercícios anteriores sobre números binários, monte um algoritmo para converter uma *string* válida de seis caracteres representando uma cor em código hexadecimal para a notação RGB, ou seja, os três inteiros $0 \le R,\,G,\,B \le 255$ com as tonalidades de vermelho, verde e azul. Implemente também a conversão no sentido contrário, ou seja, dados três inteiros $R,\,G,\,B \in [0,\,255]$, determine o código hexadecimal da cor em questão.
