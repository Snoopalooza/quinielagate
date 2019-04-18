# quinielagate
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqDlxwMhEMPJ_ln7ophiav9eF4t1-cd7u6cPlwYNmpoHeJYc4IZQ)

Pretendemos conseguir una predicción lo más ajustada posible a la realidad de los resultados de las próximas quinielas en base a los resultados a lo largo de la historia de todos los partidos jugados en la liga española, con reflejo en la propia quiniela (solo partidos en los que se puede apostar)

- **Algoritmo**: será un algoritmo simple que recorra todos los partidos jugados en la historia de la liga (últimos 10 años por ejemplo) y almacene una media de los resultados de cada partido, teniendo en cuenta quién ganó o si empataron. Por ejemplo:
{“FCB - RCBB”, “1X211X12”} la estructura de datos aún está por definir.
- **Check de resultados**: para un primer check de nuestra predicción podremos hacer comparaciones con las predicciones que hace la propia Quiniela.
- **Media con pesos**: usaremos pesos para medir la media del partido en cuestión a lo largo de la historia. Siendo D = (la diferencia entre el año actual y el año del resultado) calcularemos los pesos como 1 - D. TBC
- **Data source**: Web scraping de la matriz del final de página por tantas temporadas como queramos: https://www.bdfutbol.com/es/t/t2016-17.html
- **Framework**: Python Pandas

### Consideraciones: 
- Deberíamos crear el modelo para que se alimente de partidos y no de jornadas, de igual forma la predicción sería sobre un partido y no sobre una jornada entera.
- Modelar los empates es complicado, porque solo ganarían peso si antes ha sucedido un empate, por ello merece la pena probar de modelar con los goles del partido. Así tendríamos que el empate gana peso si ha habido resultados próximos y no simples empates exactos. (podríamos outputear la predicción de goles con una probabilidad, nos ayudaría a hacer varias quinielas cuando los resultados sean parejos probabilísticamente)
