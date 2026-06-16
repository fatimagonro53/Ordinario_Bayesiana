import random

caras = 0

for i in range(1000):
    if random.choice(["cara","cruz"]) == "cara":
        caras += 1

print("Probabilidad estimada:", caras/1000)
