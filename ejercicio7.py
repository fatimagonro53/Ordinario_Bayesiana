valores = [1,2,3,4,5,6]

media = sum(valores)/len(valores)

varianza = sum((x-media)**2 for x in valores)/len(valores)

print("Varianza:", varianza)
