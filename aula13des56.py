#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre.
#A média de idade do grupo.
#Qual o nome do homem mais velho.
#Quantas nulheres têm menos de 20 anos.
lista_idade = []
for c in range (1,5):
    nome = str (input('Qual o seu nome?'))
    idade = int(input('Qual sua idade?'))
    sexo = str(input('Qual seu sexo?'))
    lista_idade.append(idade)
    
soma = sum(lista_idade)
media = soma / len(lista_idade)
print(f'A média de idade do grupo tem a {media}')

    