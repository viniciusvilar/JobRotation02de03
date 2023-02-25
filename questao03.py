"""
Autor: Vinícius Vilar de Morais
Github: https://github.com/viniciusvilar

Questão: 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

daysWithValue0 = sumValues = amountDaysWithMoreMoney = 0
daysWithMoreMoney = []
maxValue = dados[0]["valor"]
dayMaxValue = dados[0]["dia"]
minValue = dados[0]["valor"]
dayMinValue = dados[0]["dia"]


for c in range(0, len(dados)):
    if dados[c]["valor"] == 0:
        daysWithValue0 += 1
    sumValues += dados[c]["valor"]
    if dados[c]["valor"] > maxValue and dados[c]["valor"] != 0:
        maxValue = dados[c]["valor"]
        dayMaxValue = dados[c]["dia"]
    if dados[c]["valor"] < minValue and dados[c]["valor"] != 0:
        minValue = dados[c]["valor"]
        dayMinValue = dados[c]["dia"]
    

daysWithoutDaysWithValue0 = len(dados) - daysWithValue0
mensalAverage = sumValues / daysWithoutDaysWithValue0

for c in range(0, len(dados)):
    if dados[c]["valor"] > mensalAverage:
        amountDaysWithMoreMoney += 1
        daysWithMoreMoney.append(dados[c]["dia"])

print("Quantidade de dias com faturamento acima da média mensal: {}".format(amountDaysWithMoreMoney))
print("Dias com faturamento acima da média mensal: {}".format(daysWithMoreMoney))
print("Menor valor de faturamento: R${:.2f} no dia {}".format(minValue, dayMinValue))
print("Maior valor de faturamento: R${:.2f} no dia {}".format(maxValue, dayMaxValue))
    
