# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 📝 Tu Solución

https://www.youtube.com/watch?v=SRCqFla46QQ


### Base conceptual:

Cualquier solución óptima puede ser representada en alguna de las siguientes opciones:
    
    1. Todos los paneles en posicion horizontal 
    2. Todos los paneles en posicion vertical
    3. Una mezcla de ambas. 

En los primeros dos casos, le llamaremos solución homogénea, ya que todos los paneles tienen la misma orientación. En el tercer caso, es importante notar que siempre es posible reorganizar los paneles de modo que el techo pueda dividirse mediante un único corte recto, con sentido vertical u horizontal. Todos los paneles a cada lado del corte tienen la misma orientación, lo que permite tratar cada lado como una región que tiene una única solución homogenea


Con esto en mente, el algoritmo se basa de dos partes. En la primera, se realizan distintos cortes verticales posibles del techo. Para cada corte, se divide el área en dos subregiones, izquierda y derecha. En cada una de ellas se calcula la mejor solución homogénea posible, y luego se suman ambas cantidades. Guardamos el máximo número de paneles obtenido entre todos los cortes evaluados. 

La segunda etapa es análoga, pero consiste en realizar cortes horizontales. Finalmente, la función retorna el máximo entre la mejor solución obtenida con cortes verticales y la mejor solución obtenida con cortes horizontales.
