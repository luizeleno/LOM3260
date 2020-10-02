---
nav_order: 22
dificuldade: 25
tags: [cond, loop, string, func]
mathjax: true
title: Senha forte
label: senhaforte
---

Adapte o exercício anterior para gerar uma *senha forte*, tendo pelo menos 8 caracteres, pelo menos uma letra maiúscula, pelo menos uma letra minúscula, e pelo menos um número. Conte e exiba o número de tentativas que foram necessárias antes que uma senha forte fosse gerada.

<!-- more -->

### Solução

A solução proposta abaixo faz extenso uso de [**funções**]({{site.baseurl}}/tema3/funcoes/). Apesar de não ser obrigatório, isso ajuda e muito a organização do código! Além disso, a solução apresentada aqui é ligeiramente diferente daquela que montamos em sala de aula. Compare para ver as diferenças. A principal delas é como fizemos as comparações. Veja que o comando `'A' <= c <= 'Z'`, sendo `c` um caractere (uma dado do tipo _string_) é equivalente a `65 <= ord(c) <= 90`, que foi o que usamos em aula.

```python
import numpy.random as rd

def gera_senha():
    '''
    função com a solução do ex anterior
    gera uma senha de tamanho 7-10
    com caracteres ASCII no intervalo 33-126
    '''
    L = rd.randint(7, 11)  # tamanho da senha
    s = rd.randint(33, 127, size=L)
    senha = ''.join(chr(c) for c in s)
    return senha

def verifica_senha(senha):
    '''
    função para verificar se a senha tem pelo menos:
    - 8 caracteres
    - uma letra maiúscula
    - uma letra minúscula
    - um número
    '''
    # verificando o tamanho
    if len(senha) < 8:
        return False
'A' <= c <= 'Z'
    # verificando presença de caracteres
    flag_M, flag_m, flag_n = False, False, False
    for c in senha:
        if 'A' <= c <= 'Z':
            flag_M = True  # o caractere é maiúsculo
        if 'a' <= c <= 'z':
            flag_m = True  # o caractere é minúsculo
        if '0' <= c <= '9':
            flag_n = True  # o caractere é dígito

    if flag_M == True and flag_m == True and flag_n == True:
        return True
    else:
        return False

def senha_forte():
    '''
    função para gerar uma senha forte
    usando as funções anteriores
    retorna também o número de chamadas à função gera_senha()
    '''
    n = 1
    while True:
        senha = gera_senha()
        if verifica_senha(senha) == True:
            return senha, n
        n += 1

# Chamando a função
SenhaForte, n = senha_forte()
print(f'Senha: {SenhaForte}\nTentativas: {n}')
```

:bulb: Em strings, `\n` é um código para quebra de linha. Ele corresponde ao caractere de no. 10 da [Tabela ASCII](https://pt.wikipedia.org/wiki/ASCII){: target="\_blank"}
{: .alert .alert-success }
