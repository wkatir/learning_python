class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        """Calcula el área del círculo usando la fórmula πr²."""
        return 3.1415 * (self._radius ** 2)

    @property
    def radius(self) -> float:
        """Devuelve el radio del círculo."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Establece el radio del círculo, validando que no sea negativo."""
        if value < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radius = value
    

# Ejemplo de uso:
circle = Circle(5)
print(circle.area)   # Imprime el área del círculo con radio 5

circle.radius = 10
print(circle.area)   # Imprime el área del círculo con radio 10
