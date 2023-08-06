nomeCompleto = input("Digite seu nome completo : \n").strip()

print(nomeCompleto.upper())  # tudo em letras mauisculas
print(nomeCompleto.lower())  # tudo em letras minusculas
print(len(nomeCompleto) - nomeCompleto.count(' '))  # quantas letras seu nome tem sem considerar os espacos
print(nomeCompleto.find(' '))  # quantas letras tem seu primeiro nome


