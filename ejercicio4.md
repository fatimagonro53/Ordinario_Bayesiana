# Ejercicio 4: Probabilidad Condicional

## Enunciado

Se extrae una carta de una baraja de 52 cartas. Si la carta es roja, ¿cuál es la probabilidad de que sea un corazón?

## Paso 1

Cartas rojas = 26

Corazones = 13

## Paso 2

Aplicar la fórmula:

P(A|B) = P(A∩B) / P(B)

## Resultado

P(Corazón|Roja) = 13/26

P(Corazón|Roja) = 0.5

## Código Python

```python
corazones = 13
rojas = 26

probabilidad = corazones / rojas

print(probabilidad)
```
