#CONTADOR 
positivoos = [int(input("digíte um inteteiro:")) for _ in range(5)] #receber valor
total = [par for par in positivoos if par % 2 == 0] #mostra os pares 
print('{} valores pares' .format(len(total)))

