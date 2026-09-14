respostaCerta = False

while respostaCerta == False:
    ano = int(input("Qual ano deve ser conferido?\n"))

    if ano < 0:
        print("Escreva um ano válido!")
    else:
        respostaCerta = True

def calculaAnoBissexto(ano):
    if (ano % 4 == 0 and ano % 100 == 0) or (ano % 400 == 0):
        print("O ano", ano, "é bissexto!")
    else:
        print("O ano", ano, "não é bissexto!")

calculaAnoBissexto(ano)