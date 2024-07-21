def contar_vogais(string):
   
    
    vogais = "aeiouAEIOU"
    contador = 0
    for p in string:
        if p in vogais:
            contador += 1
    return contador

string = input("Digite uma palavra: ")
numero_vogais = contar_vogais(string)
print(f"essa palavra contém {numero_vogais} vogais.")
