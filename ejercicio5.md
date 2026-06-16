# Ejercicio 5: Teorema de Bayes

## Enunciado

Una prueba médica tiene 95% de sensibilidad y 90% de especificidad. La enfermedad afecta al 1% de la población. ¿Cuál es la probabilidad de que una persona tenga la enfermedad si dio positivo?

## Paso 1

P(E) = 0.01

P(+|E) = 0.95

P(+|No E) = 0.10

## Paso 2

Aplicar Teorema de Bayes.

## Resultado

P(E|+) ≈ 0.0876

## Código Python

```python
p_e = 0.01
p_pos_e = 0.95
p_pos_noe = 0.10

resultado = (p_pos_e * p_e) / ((p_pos_e * p_e) + (p_pos_noe * (1 - p_e)))

print(resultado)
```
