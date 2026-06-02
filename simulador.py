meta= 100000.00
aporte_mensal = 1000.00

investimentos = {
    "poupanca": 0.06,
    "tesouro selic": 0.10,
    "cdb": 0.11,
    "Acoes": 0.13
}

relatorio = []


print(f"{'modalidade':<13} | {'meses':<8} | {'saldo final'}")
print("-"*40)

for nome, taxa_anual in investimentos.items():
    saldo = 0
    meses = 0
    taxa_mensal = (1+taxa_anual)**(1/12)-1
    while saldo<meta:
        saldo = (saldo + aporte_mensal)*(1+taxa_mensal)
        meses += 1

    print(f"{nome:<13} | {meses:<6} | R$ {saldo:,.2f}")

    texto_resultado = f"Levará {meses/12:.1f} anos investindo em {nome}"
    relatorio.append(texto_resultado)

print("-" * 30)
print("RELATÓRIO FINAL DE INVESTIMENTOS")
print("-" * 30)

for item in relatorio:
    print(item)
    