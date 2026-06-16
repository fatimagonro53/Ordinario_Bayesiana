# Ejercicio 7: Varianza

## Enunciado

Calcular la varianza de un dado justo.

## Fórmula

Var(X) = E(X²) - [E(X)]²

## Resultado

Var(X) ≈ 2.92

## Código Python

```python
valores = [1,2,3,4,5,6]

media = sum(valores)/len(valores)

varianza = sum((x-media)**2 for x in valores)/len(valores)

print(varianza)
```
