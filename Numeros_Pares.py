contador = 0
for n in range(1,51):
    if n % 2 == 0:
        print(n)
        contador +=1

print(f"Total de pares: {contador}")