import math

# num = int(input("Digite um num:"))
# raiz = math.sqrt(num)
# print(f"A raiz de {num} é {raiz:2f}")

# graus = 45
# radiano = graus / 180 * math.pi
# seno = math.sin (radiano)
# print(seno)

import random
num_random = random.random()
print(num_random*10)

num_random_int = random.randit(a:1, b:10)
print()

def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

print(type(print_lyrics))

#-------------------------------
#ESTRUTURA CONDICIONAL SIMPLES
#-------------------------------

 # nota = 7.0
 #
 # if nota < 8:
 #     print(f"Sua nota é: {nota}")
 #
 #     print("FIM")

nota_final = 9

if nota_final < 8:
    print("Reprovado")

else:
    print("Aprovado")

    print("FIM")

    # escolha_usuario = 121
    #
    # match escolha_usuario:
    #     case 0:
    #         status = "Sair do programa"
    #     case 1:
    #         status = "Entrar no programa"
    #     case _:
    #         status = "Erro"
    # print(status)
    #
    # DESAFIO
    idade = int(input("Digite sua idade:"))

    if idade < 16:
        print("Você ainda não pode votar")
elif 16 <= idade < 18 or idade >= 70:
print("Seu voto é opcional.")
else
print("O voto é obrigatório")