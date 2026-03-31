# Proyecto de seguimiento y alertas del Sistema Integrado de Compras Públicas (SICOP) de Costa Rica

- Todas las compras serán resumidas con ayuda de un LLM para mayor compresión de la compra, sin embargo, todas las compras serán reportadas inéditas, sin procesamiento alguno.
- Las compras "alerta" serán aquellas cuyo monto sobrepase un umbral definido por la valla superior de Tukey, la cual es una medida estadística que permite establecer un valor de referencia como “valor atípico”.

Su fórmula está dada por:

Q3 + 1.5 × IQR

Donde:
- Q3: tercer cuartil  
- IQR: rango intercuartílico (Q3 − Q1)
