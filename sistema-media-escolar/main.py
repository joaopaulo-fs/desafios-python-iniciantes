notas = []

for n in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {n}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

media = sum(notas) / len(notas)

if media >= 7:
    print(f"A média é {media:.1f} e o aluno está aprovado!")
elif 5 <= media <= 6.9:
    print(f"A média é {media:.1f} e o aluno está de recuperação!")
else:
    print(f"A média é {media:.1f} e o aluno está reprovado!")
