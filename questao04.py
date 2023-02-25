"""
Autor: Vinícius Vilar de Morais
Github: https://github.com/viniciusvilar

Questão: 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""

def percentual (value):
    percentualCalculated = 0
    percentualCalculated = (value * 100) / turnoverIncrease
    return percentualCalculated

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
others = 19849.53

turnoverIncrease = sp + rj + mg + es + others

percentualSp = percentual(sp)
percentualRj = percentual(rj)
percentualMg = percentual(mg)
percentualEs = percentual(es)
percentualOthers = percentual(others)

print("Percentual de SP: {:.2f}".format(percentualSp))
print("Percentual de RJ: {:.2f}".format(percentualRj))
print("Percentual de MG: {:.2f}".format(percentualMg))
print("Percentual de ES: {:.2f}".format(percentualEs))
print("Percentual de outros estados:: {:.2f}".format(percentualOthers))
