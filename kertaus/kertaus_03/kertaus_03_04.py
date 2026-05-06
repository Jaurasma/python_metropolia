from math import sqrt

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

if __name__ == "__main__":
    x1 = float(input("Anna ensimmäisen pisteen x-koordinaatti: "))
    y1 = float(input("Anna ensimmäisen pisteen y-koordinaatti: "))
    x2 = float(input("Anna toisen pisteen x-koordinaatti: "))
    y2 = float(input("Anna toisen pisteen y-koordinaatti: "))

    point1 = create_point(x1, y1)
    point2 = create_point(x2, y2)

    print(f"Piste 1: {point1}")
    print(f"Piste 2: {point2}")
    print(f"Pisteiden välinen etäisyys: {distance(point1, point2):.2f}")