senha = input("Crie uma senha: ")

tem_numero = False
tem_maiscula = False

for caracter in senha:
    if caracter in "0123456789":
        tem_numero = True
    if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        tem_maiscula = True

if len(senha) >= 8 and tem_numero and tem_maiscula:
    print("Senha forte!")
else:
    if len(senha) <8:
        print("Use pelo menos 8 caracteres")
    if not tem_numero:
        print("- Inclua pelo menos um número")
    if not tem_maiscula:
        print("- Inclua pelo menos uma letra maiúscula")