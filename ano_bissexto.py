def fn_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano_verificar = int(input("Qual ano deseja saber se é bissexto?\n"))

if fn_bissexto(ano_verificar):
    print(f"{ano_verificar} é bissexto")
else:
    print("Poxaaa que triste! =(\n" + f"{ano_verificar} não é um ano bissexto")
