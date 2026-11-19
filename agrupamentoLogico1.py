# Desenvolva um programa em Python que solicite o nome do aluno,
# #armazene 5 notas em uma lista (vetor) e receba o percentual  de frequência do aluno.

# O programa deve:

# Ler o nome do aluno.
# Receber as 5 notas e armazená-las em uma lista.
# Receber a frequência do aluno em percentual.
# Calcular a média das notas.
# Exibir o nome do aluno, a média e a frequência.
# Determinar a situação do aluno conforme as regras:
# Aprovado: média maior ou igual a 7,0 e frequência maior ou igual a 75%;
# Recuperação: média entre 5,0 e 6,9 e frequência maior ou igual a 75%;
# Reprovado por Nota: média menor que 5,0 e frequência maior ou igual a 75%;
# Reprovado por Falta: frequência menor que 75%, independentemente da média.
# Apresentar a situação final do aluno.

print(".:Sistema de Notas e frequencia do Aluno:.")

nome = (input("Digite o nome do Aluno:")) # atribuir uma variável nome

freq = 75 

notas =[] # notas recebe um vetor
for i in [5]:
    nota = float(input(f"Digite a {i+1} nota: ")) # Variavel nota recebe valor decimal
    notas.append(nota) #nota ao final do vetor das notas
    
freq = int(input("Digite a frequência do aluno: "))
#sum soma notas e len pega o tamnanho do vetor
media = sum(notas) / len(notas)

# avaliar resultado final com média e freq.
if media >= 7 and freq >= 75:
    resultado = "aprovado"
elif freq < 75:
    resultado = "reprovado por falta"
else:
    resultado = "reprovado por nota"

print("\n--- Resultado Final ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Frequência: {freq:.1f}%")
print(f"Situação final: {resultado}")








