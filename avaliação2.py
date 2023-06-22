#Agatha Winny Sabino Vrechi-Aumento de salário
salario = float(input("Digite seu salario: "))
aumento = float(input("Digite seu aumento em porcentagem: "))
#Criação das duas variaveis, uma "normal" e a outra para o aumento em %

reajuste = salario * aumento/ 100
#O aumento foi divido por 100 para depois ser acrescentado ao salario para mostrar o reajuste

soma = salario + (salario/100 * aumento)
#soma do salario com ele mesmo dividido por 100 vezes a % para dar o total.
print(f"Novo salario : {soma} ")
print(f"Reajuste ganho : {reajuste} ")
print(f"Em percentual : {aumento}")



