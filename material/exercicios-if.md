---
title: Exercícios sobre condicionais
parent: exs
nav_order: 0
mathjax: true
remove_trinket: false
#resolvidos: ['1', '4']
#resolvidos: ['1', '2', '3', '4', '5', '6', '10', '12', '13', '14', '15', '16', '17', '18', '20', '21', '22', '25', '28', '29']
#entrega1: ['9', '13', '14', '18', '19', '20']
#entrega2: ['30']
#entrega3: ['26']
timestamp: 04/03/26
labels: false
---

## Exercício 1: Categoria por Idade

Crie um script que receba a idade de uma pessoa (em anos) e imprima a categoria na qual ela se encaixa:

* Menor de 12 anos: "Criança"
* Entre 12 e 17 anos: "Adolescente"
* Entre 18 e 59 anos: "Adulto"
* 60 anos ou mais: "Idoso"

**Dica:** Esta é uma ótima oportunidade para encadear condições usando `if`, `elif` e `else`.`

## Exercício 2: Aprovação Escolar

Na USP, um aluno precisa ter nota maior ou igual a 5.0 e presença maior ou igual a 70% para ser aprovado. Escreva um programa que receba a nota e a porcentagem de presença do aluno e exiba:

* "Aprovado" se atender a ambos os critérios.
* "Reprovado por nota" se não atender apenas o critério de nota.
* "Reprovado por frequência" se não atender apenas o critério de presença.
* "Reprovado por ambos" se não atender ambos os critérios.

**Dica:** Use o operador lógico `and `para checar as duas condições na mesma linha.

## Exercício 3: O Maior de Três

Faça um programa que leia três números inteiros e mostre na tela qual deles é o maior.

**Dica 1:** Você pode resolver isso usando operadores lógicos para testar se um número é maior que o segundo e também maior que o terceiro ao mesmo tempo.

**Dica 2:** Para ler três números de uma só vez, use o seguinte fragmento de código:

```python
num1, num2, num3 = map(int, input("Digite três números separados por espaço:").split())
```
## Exercício 4: Calculadora de Descontos

Uma loja está dando descontos progressivos de acordo com o valor da compra:

* Compras até R$ 50,00: Sem desconto (paga o valor integral).
* Compras acima de R$ 50,00 até 100,00: 5% de desconto.
* Compras a partir de R$ 100,00: 10% de desconto.

Escreva um programa que receba o valor total da compra do cliente e calcule e exiba o valor final a ser pago com o desconto aplicado.

