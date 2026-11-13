# Exercício 3  
# Crie um programa que peça ao usuário para digitar um número e uma palavra (string). 
# Compare o número com a string utilizando os operadores == e !=. Converta o número para 
# uma string antes da comparação.

numero = input("digite um número: ")
palavra = input("Digite uma palavra: ")

if len(numero) == len(palavra):
    print("{numero} é igual a {palavra}")
if numero != palavra:
    print("{numero}")