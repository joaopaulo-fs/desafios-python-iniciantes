while True:
  try:
    numero = int(input("Digite um número: "))
    break
  except ValueError:
    print("Entrada inválida! Digite um número.")

for tabuada in range(1, 11):
    print(f"{numero} x {tabuada} = {numero * tabuada}")
