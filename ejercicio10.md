# Ejercicio 10: Simulación Monte Carlo

## Enunciado

Simular 1000 lanzamientos de moneda y estimar la probabilidad de obtener cara.

## Resultado

La probabilidad estimada se aproxima a 0.5.

## Código Python

```python
import random

caras = 0

for i in range(1000):
    if random.choice(["cara","cruz"]) == "cara":
        caras += 1

print(caras/1000)
```
