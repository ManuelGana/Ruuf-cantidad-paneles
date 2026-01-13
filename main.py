from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    """
    Calcula la cantidad máxima de paneles solares que se pueden colocar
    en un techo de dimensiones dadas, considerando que todos los paneles 
    tienen las mismas dimensiones y pueden ser colocadas en cualquier orientación 

    Para calcularlo tenemos las siguientes posibles soluciones optimas
        1. Caso homogeneo: Todos los paneles se colocan con la misma orientación
        (vertical u horizontal).
        2. Existe una mezcla de orientaciones. En este caso basta con
        hacer un único corte recto del techo (vertical u horizontal)
        y cada uno resolverse usando una solución homogénea.

    Notar que el caso homogéneo es un caso particular del segundo
    """

    return max(
        max_panels_with_cut("vertical", panel_width, panel_height, roof_width, roof_height),
        max_panels_with_cut("horizontal", panel_width, panel_height, roof_width, roof_height),
    )

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

def possible_cuts(roof_length: int, panel_width: int, panel_height: int) -> set[int]:
    """
    Devuelve todos los cortes válidos dentro de una dimensión del techo.
    """
    cuts = set()

    for i in range(1, roof_length // panel_width + 1):
        cuts.add(i * panel_width)

    for i in range(1, roof_length // panel_height + 1):
        cuts.add(i * panel_height)

    return cuts


def max_homogeneous_panels(panel_width: int, panel_height: int,
                         roof_width: int, roof_height: int) -> int:
    """
    Máxima cantidad de paneles usando una sola orientación
    (todos normales o todos rotados).
    """
    return max(
        (roof_width // panel_width) * (roof_height // panel_height),
        (roof_width // panel_height) * (roof_height // panel_width)
    )

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")

def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()

if __name__ == "__main__":
    main()
