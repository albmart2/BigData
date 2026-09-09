# Caso práctico: el rating de empresas — Respuestas

## 1. ¿Es razonable el modelo? ¿Cómo evaluarlo?

No del todo. Con 86 empresas y 40 variables (≈2 obs/variable), el R² de 0,932 es sospechosamente alto: es overfitting, no una relación real. Además, casi ninguna variable es significativa individualmente (la mayoría con p > 0,05), y la variable objetivo (beta de mercado) es un proxy débil del riesgo de crédito real (impago/bancarrota).

Cómo evaluarlo: validación fuera de muestra (train/test o cross-validation), comparar contra datos reales de impago, y no fiarse solo del R² in-sample.

## 2. ¿Cómo mejorar el modelo?

- Usar un target real de impago (bureau de crédito) en vez de la beta.
- Reducir variables (selección/LASSO) para evitar sobreajuste.
- Revisar multicolinealidad entre variables muy parecidas.
- Ampliar la muestra (más empresas, más años, distintos ciclos económicos).
- Segmentar por sector.
- Si el target pasa a binario (impago sí/no), usar regresión logística u otro clasificador, no OLS.
- Validar siempre con datos fuera de muestra.

## 3. Suponiendo que el modelo es bueno

1. Predicción → letras: se ordena a las empresas según la predicción y se dividen en tramos (percentiles) siguiendo la misma tabla de la Figura 1 (AAA, AA+, ... D), igual que se hizo con el bucketing de las variables independientes.

2. ¿Dónde lo aplica una pyme?: para negociar financiación bancaria, mejorar su balance de forma activa, compararse con su sector, evaluar a proveedores/clientes, o mostrar solvencia a inversores.

3. ¿Quién paga? ¿Conflicto de interés?: si paga la empresa evaluada (como Moody's/S&P/Fitch), hay riesgo de sesgo hacia notas favorables. Si paga quien consulta el rating, hay menos conflicto pero poco mercado dispuesto a pagar por pymes. Cobrar caro, en cualquier caso, contradice el objetivo de dar acceso barato a pymes.

4. Rentabilizar un producto barato: la clave es la automatización (scraping + ML) para que el coste marginal por informe sea casi cero y se pueda ganar por volumen. Otras vías: informes agregados/benchmarking a bancos e inversores, suscripciones, freemium. Si además se vende consultoría de mejora a la misma empresa calificada, reaparece el conflicto de interés, así que conviene separar ambas actividades.
