while True:
    try:
        numero_1 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Por favor! Digite um número.")

while True:
    try:
        numero_2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Por favor! Digite um número.")

while True:
    operacao = input("Digite a operação que deseja realizar (+, -, *, /): ").lower()
    if operacao in ["+", "-", "*", "/"]:
        break
    else:
        print("Digite uma operação válida.")

if operacao == "+":
    print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
elif operacao == "-":
    print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
elif operacao == "*":
    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
else:
    if numero_2 == 0:
        print("Não é possivel realizar divisão por 0.")
    else:
        print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
