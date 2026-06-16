# Ejercicio 3: Unión de eventos

## Enunciado

Se lanza un dado. ¿Cuál es la probabilidad de obtener un número par o un número mayor que 4?

## Paso 1

Números pares:

{2,4,6}

Números mayores que 4:

{5,6}

## Paso 2

Unión:

{2,4,5,6}

## Resultado

P(A∪B) = 4/6

P(A∪B) = 0.6667

## Código Python

```python
favorables = 4
posibles = 6

probabilidad = favorables / posibles

print(probabilidad)
```
