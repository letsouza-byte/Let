quantidade = 0
total = 0

valor = float(input("Digite o valor da venda (0 para encerrar): R$ "))

while valor != 0:
    if valor < 0:
        print("Valor inválido, venda ignorada.")
    else:
        quantidade += 1
        total += valor
    valor = float(input("Digite o valor da venda (0 para encerrar): R$ "))

print("Quantidade de vendas: ", quantidade)
print("Total vendido: R$ ", total)