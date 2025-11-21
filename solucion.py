# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    if m < 0:
        return print("Error: La altura debe ser un entero positivo")

    for i in range(-m+1, m):
        h = m - abs(i)
        print(s * h)