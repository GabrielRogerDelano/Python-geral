frase = 'Curso em Video de Python'

# fatiamento: list[onde inicia : onde termina : de quanto em quanto

print(frase[0::2])  # Croe ie ePto

# Analise
print(len(frase))  # 24
print(frase.count('o'))  # 3

# quando o find() retorna -1 quer dizer que nao escontrou a sentenca, quando encontra retorna a posicao em que comeca
print(frase.find('Python'))  # 18

# quando quer receber so se existe a palavra q deseja
print('Curso' in frase)  # True

# trocar palavras usase o replace
fraseComJava = frase.replace("Python", "java")
print(fraseComJava)  # Curso em Video de java

# UpperCase
print(frase.upper())  # CURSO EM VIDEO DE PYTHON

# LowCase
print(frase.lower())  # curso em video de python

# capitilize deixa so a primeira letra mauiscula
print(frase.capitalize())  # Curso em video de python

# title deixa todo inicio de palavra em mauiscula
print(frase.title())  # Curso Em Video De Python

# strip remove todos os espacos inuteis
novaFrase = '    varios espacos       '
print(novaFrase)  #     varios espacos
print(novaFrase.strip()) # varios espacos

# split gera uma lista com todas as palavras da frase, depois ver mais propriedades dessa funcao
print(frase.split())  # ['Curso', 'em', 'Video', 'de', 'Python']

# join junta as palavras usando o separador que voce escolher
print('='.join(frase))  # C=u=r=s=o= =e=m= =V=i=d=e=o= =d=e= =P=y=t=h=o=n
print('_'.join(frase.split()))  # Curso_em_Video_de_Python

