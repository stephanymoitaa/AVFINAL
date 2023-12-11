positivos = [float(input("digite os valores:")) for _6
    in range(6)] #colocar em for in range para a contagem.
totalpositivos = 0 
somadosposit = 0 

for s in positivos:
    if s > 0:
        totalpositivos += 1 #contagem de positivos 
        somadosposit += s #soma deles 
print('{} valores positivos' .format(totalpositivos))
print('{:.if}'.format(somadosposit/totalpositivos))