arquivo = open("Python.txt", "r")
tamanho = 14
palavras_maiores = []

for a in arquivo.readlines():
    for palavra in a.strip().split():
        if len(palavra) > tamanho:
            tamanho = len(palavra.replace(".", "")) - 1
            palavras_maiores.append(palavra.replace(".", ""))


print(tamanho)
print(palavras_maiores)