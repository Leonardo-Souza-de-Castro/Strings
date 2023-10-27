frase = input("Digite uma frase: ")
saida = ""

frase = frase.replace(" ", "") # A função replace substitui caracteres por um que você desejar

for a in range(len(frase)):
    saida += frase[-a-1]

if frase == saida:
    print("A frase digitada é um palindromo")
else:
    print("A frase digitada não é um palindromo")