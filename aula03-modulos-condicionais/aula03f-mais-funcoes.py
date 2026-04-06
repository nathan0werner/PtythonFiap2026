# def boas_vindas(nome)
#     print(f"Olá, {nome}! Seja bem-vindo!")
#
# nome_digitado - input("Digite seu nome: ")
# boas_vindas(nome_digitado)
#
# def soma(num_a, num_b):
#     soma = num_a + num_b
#     return soma
#
# resultado_soma = soma(5, 3)
# print(resultado_soma)

# Exercicios
#2
# numero = int(input("Digite um número: "))
#
# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

#3
# num1 = float(input("Digite o primeiro número:"))
# num2 = float(input("Digite o segundo número:"))

# if num1 > num2:
#     print("O maior número é", num1)
# elif num2 > num1:
#     print("O maior número é", num2)
# else:
#     print("Os dois números são iguais")
#

#4
# nota1 = float(input("Digite a primeira nota:"))
# nota2 = float(input("Digite a segunda nota:"))
# nota3 = float(input("Digite a terceira nota:"))
# nota4 = float(input("Digite a quarta nota:"))
#
# media = (nota1 + nota2 + nota3 + nota4) / 4
# print(f"Média: {media:.2f}")
#
# if media >= 7:
#     print("Aprovado")
# elif media >= 5:
#     print("Em recuperação")
# else:
#     print("Reprovado")

#5
# A = int(input("Digite o valor de A:"))
# B = int(input("Digite o valor de B:"))
#
# if A % B == 0 or B % A == 0:
#     print("São Múltiplos")
# else:
#     print("Não são múltiplos")
#

#6
# Leitura dos dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

# Verificação e cálculo
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Exibição do resultado
print("Resultado:", resultado)