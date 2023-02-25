"""
Autor: Vinícius Vilar de Morais
Github: https://github.com/viniciusvilar

Questão: 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

name = input("Informe uma palavra: ")
reverseName = ""
lengthName = -1

for c in name:
    lengthName += 1


while lengthName >= 0:
    reverseName += name[lengthName]
    lengthName -= 1

print(reverseName)