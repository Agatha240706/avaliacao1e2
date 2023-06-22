#Agatha Winny Sabino Vrechi- Média Ponderada
n = int(input("Digite o número de casos: "))

# vai ler os 3 valores
for c in range(n):
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    # Calcular a média ponderada
    media = (valor1 * 2 + valor2 * 3 + valor3 * 5) / 10

    # Exibir o resultado da média ponderada
    print(f"A média ponderada é: {media:.1f}")