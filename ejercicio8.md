# Ejercicio 8: Distribución Binomial

## Enunciado

¿Cuál es la probabilidad de obtener exactamente 3 caras en 5 lanzamientos de moneda?

## Datos

n = 5

x = 3

p = 0.5

## Resultado

P(X=3) = 0.3125

## Código Python

```python
from math import comb

n = 5
x = 3
p = 0.5

probabilidad = comb(n,x)*(p**x)*((1-p)**(n-x))

print(probabilidad)
```
