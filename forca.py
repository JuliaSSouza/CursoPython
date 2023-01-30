palavra = input('insira uma palavra\n')
letra_alvo = list(palavra)
letra_total = 0;

for i in range(len(palavra) + 6):
    letra_escolha = input('insira uma letra\n')
    
    if letra_escolha in letra_alvo:
        letra_total += 1
        print('sim')
    else:
        print('não')                 
    if letra_total == len(letra_alvo):
       print('Parabéns! A palavra é', palavra) 
       break
else:
    print('Que pena!Não foi dessa vez')

