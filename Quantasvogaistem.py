def contar_vogais(string):
    vogais = "aeiouAEIOU"
    contador = 0
    for p in string:
        if p in vogais:
            contador += 1
    return contador

while True:
    try:
        string = input("Digite uma palavra: ")
        if not string.isalpha():
            raise ValueError("Por favor, digite apenas letras.")
        break
    except ValueError as ve:
        print(ve)

numero_vogais = contar_vogais(string)
print(f"Essa palavra contém {numero_vogais} vogais.")
