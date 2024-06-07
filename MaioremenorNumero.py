i = []
resp = 'S'
while resp in 'Ss':
    num = int(input('digite um número: '))
    resp = str(input('quer continuar [S/N] ')).upper().strip()[0]
    i.append(num)
print(f'vc digitou {len(i)} numeros e a media foi {sum(i) / len(i) }')
print(f'o maior valor foi {max(i)} e e menor valor foi {min(i)}')