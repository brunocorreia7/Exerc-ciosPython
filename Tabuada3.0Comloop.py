while True:
    n = int(input('digite um número '))
    print('-' * 30)
    if n < 0:
        break 
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 30)
print('Programa Tabuada encerrado! Volte Sempre!')
    
    
    
    