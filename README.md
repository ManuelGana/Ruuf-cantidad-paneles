# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 📝 Tu Solución

https://www.youtube.com/watch?v=SRCqFla46QQ


### Bases conceptual:

Cualquier solución óptima puede ser representada en alguna de las siguientes opciones:
    
    1. Todos los paneles en posicion horizontal 
    2. Todos los paneles en posicion vertical
    3. Una mezcla de ambas. 

En los primeros dos casos, le llamaremos solución homogénea, ya que todos los paneles tienen la misma orientación. En el tercer caso, es importante notar que siempre es posible reorganizar los paneles de modo que el techo pueda dividirse mediante un único corte recto, con sentido vertical u horizontal. Todos los paneles a cada lado del corte tienen la misma orientación, lo que permite tratar cada lado como una región que tiene una única solución homogenea


Con esto en mente, el algoritmo se basa de dos partes. En la primera, se realizan distintos cortes verticales posibles del techo. Para cada corte, se divide el área en dos subregiones, izquierda y derecha. En cada una de ellas se calcula la mejor solución homogénea posible, y luego se suman ambas cantidades. Guardamos el máximo número de paneles obtenido entre todos los cortes evaluados. 

La segunda etapa es análoga, pero consiste en realizar cortes horizontales. Finalmente, la función retorna el máximo entre la mejor solución obtenida con cortes verticales y la mejor solución obtenida con cortes horizontales.

### Código:
La función principal es:
```
def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    return max(
        max_panels_with_cut("vertical", panel_width, panel_height, roof_width, roof_height),
        max_panels_with_cut("horizontal", panel_width, panel_height, roof_width, roof_height),
    )
```

Esta función retorna la mejor solución entre cortes verticales y horizontales, evaluando cuál caben más paneles.


Luego, tenemos:

```
def max_panels_with_cut(axis: str, panel_width: int, panel_height: int,
                      roof_width: int, roof_height: int) -> int:
    max_panels = 0

    if axis == "vertical":
        cuts = possible_cuts(roof_width, panel_width, panel_height)
        for cut in cuts:
            left = max_homogeneous_panels(panel_width, panel_height, cut, roof_height)
            right = max_homogeneous_panels(panel_width, panel_height, roof_width - cut, roof_height)
            max_panels = max(max_panels, left + right)

    elif axis == "horizontal":
        cuts = possible_cuts(roof_height, panel_width, panel_height)
        for cut in cuts:
            bottom = max_homogeneous_panels(panel_width, panel_height, roof_width, cut)
            top = max_homogeneous_panels(panel_width, panel_height, roof_width, roof_height - cut)
            max_panels = max(max_panels, bottom + top)

    return max_panels
```

Lo más importante de esta función son los parámetros que le pasamos a las funciones:
- Para los cortes verticales, el “largo” que importa es el ancho del techo
- Para los cortes horizontales, el largo que importa es la altura del techo.

Luego, para cada subregión calculamos la mejor solución homogénea. Al sumar los resultados de ambas subregiones y tomar el máximo entre todos los cortes, obtenemos la mejor solución.


Además tenemos esto:
```
def possible_cuts(roof_length: int, panel_width: int, panel_height: int) -> set[int]:
    cuts = set()

    for i in range(1, roof_length // panel_width + 1):
        cuts.add(i * panel_width)

    for i in range(1, roof_length // panel_height + 1):
        cuts.add(i * panel_height)

    return cuts
```
La cual se encarga de generar todos los cortes válidos, ya sea el ancho o la altura. Un corte es válido si está entre los bordes de los paneles. Por otro lado, como los paneles pueden colocarse en dos orientaciones diferentes, estos bordes pueden encontrarse en múltiplos de panel_width o de panel_height. La función recorre ambos casos y agrega todas las posiciones posibles a un set.

Finalmente tenemos:
```
def max_homogeneous_panels(panel_width: int, panel_height: int,
                         roof_width: int, roof_height: int) -> int:
    return max(
        (roof_width // panel_width) * (roof_height // panel_height),
        (roof_width // panel_height) * (roof_height // panel_width)
    )
```

Calcula la máxima cantidad de paneles que caben en un rectángulo dado si todos los paneles tienen la misma orientación. Para esto, evalúa ambas opciones, horientación horizontal o vertical. En cada caso, se divide la dimensión del techo entre la dimensión del panel para ver cuántos caben en cada eje, y luego se multiplica para obtener el total de paneles. Finalmente, toma el máximo de ambas opciones.
