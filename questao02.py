"""
Autor: Vinícius Vilar de Morais
Github: https://github.com/viniciusvilar

Questão: 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

Info: para essa questão foi calculado os 1000 primeiros números da Sequência de Fibonnaci
"""

first = proxNumber = 0
second = 1
counter = 2
listFibonacci = [0, 1]
response = ""

number = int(input("Digite um valor inteiro: "))

while counter < 1000:
    proxNumber = first + second
    first = second
    second = proxNumber
    counter += 1
    listFibonacci.append(proxNumber)

if (number in listFibonacci):
    response = "O valor {} está na Sequência de Fibonacci!".format(number)
else:
    response = "O valor {} não está na Sequência de Fibonacci!".format(number)

print(response)