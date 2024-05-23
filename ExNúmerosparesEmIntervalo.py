número = 0
for n in range(1,21):
    if n % 2 == 0:
        número += 1
        print(n)
print(f'tem {número} números pares entre 1 e 20')