---
title: Formatação e indentação
parent: temaone
nav_order: 1
has_children: false
permalink: /docs/intro/
status: green
tags: [edição, arquivos, extensão, py, sintaxe, indentação, comentário, tabulação, formatação]
timestamp: 22/08/20
---

Um código python é escrito de maneira estruturada usando tabulações (indentação) criando blocos dentro do arquivo
{: .lead}

## Sistema de arquivos

- Arquivos legíveis por um *interpretador* python tem o formato de arquivos texto.
- Usualmente, para identificá-los, adiciona-se a *extensão* `.py` ao nome do arquivo
- Não existem muitas restrições quanto ao nome do arquivo (isso depende mais do seu sistema operacional), mas eu recomendo evitar espaços em branco e caracteres especiais e acentuados para batizar seus programas. Isso é uma garantia de maior portabilidade de seus códigos para diversas plataformas (windows, linux, mac, ...)

## Sintaxe python

Diferente de outras linguagens de programação, como C, C++ e Java, os diferentes blocos de um programa python são identificados por **tabulações**, ou espaços em branco que servem como **indentação**  (espaço em branco antes dos comandos)  e fazem o papel das chaves nas linguagens citadas. Por exemplo, o seguinte código escrito em C:
```c
/* isto é um comentário */
n = 0;
y = 0;
while(n < 10) {
  y += n;
  n++;
}
printf("y = %d\n", y)
```
é equivalente, em python, ao seguinte:
```python
# isto é um comentário
n, y = 0, 0
while n < 10:
  y += n
  n += 1
print(f'y = {y}')
```
Em C, o bloco definido pelo comando `while` é delimitado pelas chaves (`{}`). Além disso, cada comando é terminado necessariamente por um ponto-e-vírgula (`;`). A indentação dentro do bloco `while` é puramente opcional, servindo apenas para aumentar a legibilidade do código.

Em python, por outro lado, a indentação é **obrigatória**: é a maneira pela qual o python identifica quais comandos pertencem ao bloco `ẁhile` e quais não pertencem. Veja que a única diferença entre a a penúltima linha (`n += 1`) e a última (`print(f'y = {y}')`) é a falta de indentação desta última, fazendo com que ela esteja fora do `while`. Para tornar o código mais legível, seria interessante deixar uma linha em branco entre essas duas linhas.

:information_source: Em python, qualquer coisa após o símbolo `#` é um **comentário**. O intérprete python ignora essas partes do código quando executa seus programas. Comentários servem para melhor *documentar* o seu código, como observações para quem vai ler seu código e tentar entendê-lo. Inclusive para você mesmo, depois de alguns dias sem olhar para ele!
{: .alert .alert-primary}

Veja que diferentes blocos podem estar *aninhados*, novamente usando indentação. Por exemplo, considere o seguinte código:
```python
m, n, y = 0, 0, 0
while m < 10:
  while n < 10:
    y += n
    n += 1
  m += 1

print(f'y = {y}')
```
A linha `n += 1` está dentro do segundo `while`, mas a última linha (`m += 1`) está dentro do primeiro, mas fora do segundo.

Assim, um código python é, em geral, mais conciso que códigos escritos em outras linguagens semelhantes. Também por esse motivo, é preciso tomar cuidado, pois falhas na indentação podem dificultar o processo de *debugging* (eliminação de erros).
