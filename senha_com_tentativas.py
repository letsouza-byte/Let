senha_correta = "python"
tentativas = 0

while tentativas < 3:
    senha = input("Senha: ")
    tentativas += 1
    if senha == senha_correta:
        print("Acesso liberado")
        break
    print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

if senha != senha_correta:
    print("Conta bloqueada")