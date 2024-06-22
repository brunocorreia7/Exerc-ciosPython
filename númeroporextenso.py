numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", 
    "cinco", "seis", "sete", "oito", "nove", "dez"
)
numero = int(input("Digite um número entre 0 e 10: "))
if numero in range(len(numeros_extenso)):
    print(f"O número digitado foi {numero}, que por extenso é '{numeros_extenso[numero]}'.")
else:
    print("Número fora do intervalo permitido. Por favor, digite um número entre 0 e 10.")
