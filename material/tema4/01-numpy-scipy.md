---
title: Numpy e Scipy 
nav_order: 1
parent: temafour
status: green
tags: [numpy, scipy, pandas, matplotlib, array, matlab]
---

Numpy e scipy são módulos incrivelmente completos para praticamente qualquer atividade científica computacional
{: .lead }

Já sabemos como importar módulos em python, e já vimos, no primeiro tópico do Tema 3 (*Módulos*), até como usar o módulo `numpy`  para calcular a raiz quadrade de um `float`. Vamos agora ver mais detalhes sobre o `numpy` e seu irmão, o `scipy`.

`Numpy` é o acrônimo de *Numerical Python* e `Scipy`, de *Scientific Python*. Os dois formam, na verdade, um gigantesco conjunto de módulos distribuídos em conjunto sob a tutela do [`scipy.org`](https://www.scipy.org/) e [`numpy.org`](https://numpy.org/), desenvolvidos em conjunto com outros módulos, como `matplotlib` e `pandas`, que veremos em outra ocasião.

O objetivo principal dos módulos `numpy` e `scipy` é fornecer recursos básicos para a computaçao científica. Alguns exemplos:
- Funções matemáticas: trigonométricas, exponenciais e logarítmicas, funções da Física Matemática, etc.
- Recursos numéricos como zeros de funções, integração e derivação numérica, ajuste de curvas, etc.
- Ferramentas de Álgebra Linear, como determinantes, inversas, autovalores e autovetores, etc.

O recurso principal dessa família de módulos, no entanto, é um novo tipo de dado criado especificamente para lidar de modo fácil com grandes conjuntos de dados: o **array**, com forte inspiração em Matlab. Veremos mais detalhes sobre arrays em breve. Antes disso, porém, vamos vê-los em prática numa aplicação bem especícica mas extremamente importante: a geração de números aleatórios.
