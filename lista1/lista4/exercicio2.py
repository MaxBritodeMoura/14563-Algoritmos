palavra1 = input("DIgite a 1ª palavra: ")
palavra2 = input("Digite a 2ª palavra: ")

if len(palavra1) > len(palavra2):
    print(f"{palavra1} e menor que {palavra2}")
elif palavra1 == palavra2:
    print(f"{palavra2} é igual que {palavra1}")
else:
    print(f"{palavra2} é maior que {palavra1}")

