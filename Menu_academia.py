mensalidade = 250.00

while True:
    print()
    print("==== Academia Rio Fit ====")
    print("1 - Ver horário")
    print("2 - Calcular plano")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "0":
        print("Até logo!")
        break
    elif opcao == "1":
        print("Segunda a sexta, das 6h às 21h")
    elif opcao == "2":
        meses = int(input("Quantos meses? "))
        total = mensalidade * meses
        if meses >= 6:
            total = total * 0.90 #10% de desconto
        print(f"Total do plano: R$ {total}")
    else:
       print("Opção Inválida")