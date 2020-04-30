import requests
import re
from bs4 import BeautifulSoup
import datetime as dt
import matplotlib.pyplot as plt

#of = open('01-introdução.md', 'w')
of = open('teste.md', 'w')

meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio',
         6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro',
         11: 'novembro', 12: 'dezembro'}
data = dt.date.today()
mes = meses[data.month]
ano = data.year

header = '''---
title: "Introdução: python é popular!"
parent: sobre
nav_order: 0
tags: [introdução, pypl, python, popularity]
permalink: /popularidade/
timestamp: '%s'
---

Python é a linguagem mais popular e a que mais cresce mundialmente
{: .lead}

## O índice PYPL:

![]({{site.baseurl}}/assets/images/pypl.jpeg){: .col-md-8 .my-1 }

O **índice PYPL** (*PopularitY of Programming Language*) é obtido analisando \
a frequência com que busca-se por tutoriais da linguagem no Google\
([pypl.github.io/PYPL.html](http://pypl.github.io/PYPL.html)\
{: target="\\_blank"})

| Posição	| Linguagem |	Fatia	| Tendência |
|:-------:|:--------- |:-----:|:---------:|
''' % (data.strftime('%d/%m/%y'))

print(header, end='', file=of)


URL = 'http://pypl.github.io/PYPL.html'
page = requests.get(URL)
text = page.text.split('\r\n')

for L in text:
    if re.search('begin section All', L):
        L = L.replace('\\\"', '\"')
        break

soup = BeautifulSoup(L, 'html.parser')
language = soup.find_all('td', class_='')
share = soup.find_all(lambda tag: tag.name == 'td' and
                      tag.get('class') == ['right'])
trend = soup.find_all('td', class_='optCol')

for n in range(len(language)):
    print(f'| {n+1} | {language[n].string} | \
          {share[n].string[:-1]} | {trend[n].string[:-1]} |', file=of)

print(f'\n***Mundialmente em {mes} de {ano}, comparado \
      a um ano antes***', file=of)
print('{: .small}', file=of)

of.close()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
nmax = 9
labels = [n.string for n in language[:nmax]]
labels.append('Outras')
sizes = [n.string[:-1] for n in share[:nmax]]
resto = [n.string[:-1] for n in share[nmax:]]
r = sum(list(map(float, resto)))
sizes.append(str(r))
explode=[0] * (nmax+1)
# explode[0] = .1

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%', explode=explode,
        shadow=True, startangle=30)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('../../assets/images/pypl.jpeg', bbox_inches='tight')

plt.show()
