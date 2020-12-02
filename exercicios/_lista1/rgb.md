---
nav_order: 14
dificuldade: 30
tags: [loop, string, dict]
mathjax: true
title: Sistema RGB
label: rgb
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

<!-- more -->

## Solução

```python
# dicionário para conversão de decimal para hexadecimal
dec_hex_dicio = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# dicionário para conversão de hexadecimal para decimal
hex_dec_dicio = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def rgb_para_hex(rgb):
	'''
		função para conversão de cores rgb = [r, g, b]
		para uma string com os códigos hexadecimais
	'''
	code = ''
	for cor in rgb:  # iterando pelas três cores
		colorhex = ''
		while cor > 0:  # conversão para hexadecimal (mesmo algoritmo do ex. 13)
			resto = cor % 16
			cor = cor // 16
			colorhex = dec_hex_dicio[resto] + colorhex  # sobrecarga do operador + para strings
		code += colorhex
	return code


def hex_para_rgb(code):
	'''
		função para a conversão de uma string com o código hexadecimal
		para a lista rgb=[r, g, b] de cores
	'''
	cores = []  # inicializando a lista
	for c in range(0, 6, 2):  # fazendo o loop a cada dois caracteres de code
		cor = hex_dec_dicio[code[c]] * 16  # convertendo o primeiro caractere
		cor += hex_dec_dicio[code[c+1]]  # e somando o segundo
		cores.append(cor)  # adicionando cor à lista
	return cores
```
