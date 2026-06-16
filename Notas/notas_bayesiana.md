# Notas de Probabilidad Bayesiana

## Introducción

La probabilidad constituye una de las herramientas fundamentales de la ciencia actuarial, ya que permite modelar fenómenos inciertos y cuantificar riesgos. A través de los modelos probabilísticos es posible analizar eventos aleatorios, estimar pérdidas futuras, calcular primas de seguros y apoyar la toma de decisiones bajo incertidumbre.

La probabilidad bayesiana representa un enfoque que permite actualizar el conocimiento previo cuando se dispone de nueva información, convirtiéndose en una herramienta esencial para el análisis estadístico moderno.

---

# Probabilidad

La probabilidad es una medida numérica asociada a la posibilidad de ocurrencia de un evento. Sus valores se encuentran entre 0 y 1, donde 0 representa un evento imposible y 1 un evento seguro.

La probabilidad clásica se define como:

P(A) = Casos favorables / Casos posibles

Este concepto constituye la base de los modelos actuariales utilizados para estimar la ocurrencia de siniestros, accidentes o eventos financieros.

### Ejemplo

Al lanzar un dado equilibrado:

P(obtener un 4) = 1/6

---

# Regla del Complemento

En muchas aplicaciones actuariales resulta más sencillo calcular la probabilidad de que un evento no ocurra.

La regla del complemento se expresa como:

P(Aᶜ) = 1 − P(A)

Esta propiedad es ampliamente utilizada en seguros para calcular probabilidades de supervivencia, incumplimiento o ausencia de siniestros.

### Ejemplo

La probabilidad de no obtener un 6 en un dado es:

P(no obtener 6) = 1 − 1/6 = 5/6

---

# Unión de Eventos

La unión de eventos representa la ocurrencia de al menos uno de dos eventos.

Su expresión matemática es:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

La resta de la intersección evita contabilizar dos veces los resultados comunes.

Este concepto es útil cuando se analizan riesgos múltiples que pueden ocurrir simultáneamente.

---

# Probabilidad Condicional

La probabilidad condicional mide la probabilidad de ocurrencia de un evento dado que otro ya ocurrió.

Su fórmula es:

P(A|B) = P(A ∩ B) / P(B)

La probabilidad condicional es uno de los pilares de la estadística bayesiana y permite incorporar información adicional al análisis probabilístico.

### Aplicación actuarial

Puede utilizarse para estimar la probabilidad de presentar una reclamación dado que un asegurado pertenece a determinado grupo de riesgo.

---

# Independencia de Eventos

Dos eventos son independientes cuando la ocurrencia de uno no modifica la probabilidad del otro.

Matemáticamente:

P(A ∩ B) = P(A) × P(B)

La independencia es una hipótesis frecuente en modelos actuariales, aunque en la práctica debe verificarse cuidadosamente debido a posibles dependencias entre riesgos.

---

# Teorema de Bayes

El Teorema de Bayes es una herramienta que permite actualizar probabilidades a partir de nueva evidencia observada.

Su expresión es:

P(A|B) = [P(B|A) × P(A)] / P(B)

Donde:

- P(A) representa la probabilidad previa.
- P(B|A) representa la verosimilitud.
- P(A|B) representa la probabilidad posterior.

### Aplicaciones

En actuaría y seguros se utiliza para:

- Actualizar estimaciones de riesgo.
- Evaluar diagnósticos médicos.
- Analizar fraude.
- Construir modelos predictivos.

El enfoque bayesiano permite combinar experiencia previa con información reciente para obtener estimaciones más precisas.

---

# Esperanza Matemática

La esperanza matemática representa el valor promedio esperado de una variable aleatoria después de un gran número de observaciones.

Se calcula mediante:

E(X) = Σ x·P(x)

Desde la perspectiva actuarial, la esperanza matemática permite calcular pérdidas esperadas, costos futuros y primas puras de seguros.

### Ejemplo

Para un dado equilibrado:

E(X) = 3.5

---

# Varianza

La varianza mide la dispersión de una variable aleatoria respecto a su valor esperado.

Su fórmula es:

Var(X) = E(X²) − [E(X)]²

En ciencia actuarial, la varianza resulta especialmente importante porque no solo interesa conocer el valor esperado de una pérdida, sino también la incertidumbre asociada a dicha pérdida.

Una mayor varianza implica un mayor nivel de riesgo.

---

# Distribución Binomial

La distribución binomial modela el número de éxitos obtenidos en una cantidad fija de ensayos independientes.

Su función de probabilidad es:

P(X=x) = C(n,x)p^x(1-p)^(n-x)

Esta distribución tiene aplicaciones en:

- Modelos de supervivencia.
- Estudios de mortalidad.
- Frecuencia de siniestros.
- Control estadístico de calidad.

---

# Distribución Normal

La distribución normal es una de las distribuciones más importantes en estadística debido a su presencia en numerosos fenómenos naturales y económicos.

Se caracteriza por:

- Simetría alrededor de la media.
- Forma de campana.
- Definición mediante la media y la desviación estándar.

La estandarización se realiza mediante:

z = (x − μ)/σ

La distribución normal es ampliamente utilizada en modelos de riesgo, análisis financiero y estimación estadística.

---

# Variables Aleatorias

Una variable aleatoria es una función que asigna valores numéricos a los resultados de un experimento aleatorio.

## Variables Discretas

Toman valores específicos y contables.

Ejemplos:

- Número de reclamaciones.
- Número de accidentes.
- Número de asegurados.

## Variables Continuas

Pueden asumir cualquier valor dentro de un intervalo.

Ejemplos:

- Tiempo de vida de una persona.
- Monto de una pérdida económica.
- Rendimiento financiero.

Las variables aleatorias constituyen el fundamento matemático sobre el cual se desarrollan los modelos probabilísticos y actuariales.

---

# Conclusión

La probabilidad bayesiana proporciona un marco sólido para el análisis de incertidumbre y la actualización de creencias a partir de nueva información. Conceptos como probabilidad condicional, Teorema de Bayes, esperanza matemática, varianza y distribuciones de probabilidad son herramientas esenciales para la formación actuarial, ya que permiten modelar riesgos, cuantificar incertidumbre y respaldar decisiones fundamentadas en evidencia estadística.
