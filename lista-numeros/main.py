lista = []

for n in range(1, 6):
  while True:
    try:
      numero = int(input(f"Digite o número {n}: "))
      lista.append(numero)
      break
    except ValueError:
      print("Entrada inválida! Digite um número.")

print(f"Lista: {lista}\nMaior número: {max(lista)}\nMenor número: {min(lista)}\nMédia: {sum(lista) / len(lista)}")
