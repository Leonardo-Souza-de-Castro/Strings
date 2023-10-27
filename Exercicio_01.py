string = input("Digite um frase: ")
string_formatada = ""

# # Exemplo utilizando ord
for a in string:
    # O ord ele verifica qual o código decimal do caracter
    if ord(a) == 97:
        a = "A"
    elif ord(a) == 101:
        a = "E"
    elif ord(a) == 105:
        a = "I"
    elif ord(a) == 111:
        a = "O"
    elif ord(a) == 117:
        a = "U"
    string_formatada += a

print(f"Nova String: {string_formatada}")


# Exemplo do professor
vogais = ['a', 'e', 'i', 'o', 'u']

for a in string:
    if a in vogais:
        # o chr ele mostra qual o caracter com base no valor decimal dele
        string_formatada += chr(ord(a) - 32)
    else:
        string_formatada += a

print(f"Nova String: {string_formatada}")

# Exemplo bloco de string
print("""
    Olá!
    Meu nome é Leonardo
""") # as aspas triplas fazem a tabulação do print do jeito que digitamos
