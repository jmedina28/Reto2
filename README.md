<h1 align="center">Reto 2</h1>

<h3 align="center">Perfiles de GitHub de los autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
2. [@Diegodesantos1](https://github.com/Diegodesantos1)
3. [@mat0ta](https://github.com/mat0ta)
4. [@XaviTheForce](https://github.com/Xavitheforce)
5. [@ESTHERRODRIGUEZGARCIA](https://github.com/ESTHERRODRIGUEZGARCIA)

---
En este [repositorio](https://github.com/jmedina28/Reto2) queda resuelto el reto 2 en el que hemos llevado a cabo un análisis del siguiente [paper](https://arxiv.org/pdf/1811.11813.pdf).
***

## El Algoritmo SWAG; un enfoque matemático que supera el aprendizaje profundo tradicional. 

SWAG (Sparse Wrapper Algorithm). Tipo de red neuronal en el que las funciones de activación en cada capa forman una base polinomial. La función de activación se encarga de devolver una salida a partir de un valor de entrada, normalmente el conjunto de valores de salida en un rango determinado. 
Se buscan funciones que las derivadas sean simples, para minimizar con ello el coste computacional.

La primera capa de esta estructura tiene k neuronas, siendo k el mayor grado del polinomio de estimación de la función g(x) y el número de funciones de activación diferentes. La segunda capa está completamente conectada con una función de activación lineal. Y para añadir más capas, se repite el patrón de las anteriores. 
Finalmente, usando el algoritmo de propagación hacia atrás podemos encontrar el conjunto de valores que optimizan las predicciones.

El algoritmo SWAG supera y converge más rápido que el rendimiento de última generación en redes neuronales totalmente conectadas. Además es capaz de resolver problemas que las arquitecturas actuales no pueden y tienen el potencial de cambiar la forma en  que nos acercamos al aprendizaje profundo. 

![image](https://user-images.githubusercontent.com/91721860/194777539-dcacbf81-7283-4972-af85-ee69b7c1882d.png)

