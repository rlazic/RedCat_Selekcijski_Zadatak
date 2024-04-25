import numpy as np

# funkcija učitava točke iz datoteke
def read_points(file_path):
    with open(file_path, 'r') as file:
        all_points = [np.array(list(map(float, line.strip().split(', ')))) for line in file]
    return all_points

# funkcija provjerava čine li zadane točke vrhove zajedničkog kvadra
def is_cuboid(points):
    # određujemo vektore za svaki par točaka
    vectors = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            vectors[(i+1, j+1)] = points[i] - points[j]

    # funkcija provjerava jesu li vektori međusobno okomiti
    def are_perpendicular(vector1, vector2):
        return np.dot(vector1, vector2) == 0

    # provjeravamo koliko međusobno okomitih vektora sa zajedničkom točkom postoji u sustavu točaka
    perpendicular_count = 0
    for (p1, p2), vector1 in vectors.items():
        for (p3, p4), vector2 in vectors.items():
            if (p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4):
                if are_perpendicular(vector1, vector2):
                    perpendicular_count += 1
    return perpendicular_count / 2

# funkcija provjerava nalazi li se zadana točka unutar pravokutnika
def is_point_inside(points, test_point):  
    min_bound = np.min(points, axis=0)
    max_bound = np.max(points, axis=0)
    return np.all(min_bound <= test_point) and np.all(test_point <= max_bound)

# funkcija računa duljinu stranica
def vector_magnitudes(points):
    magnitudes = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            vector = points[i] - points[j]
            magnitude = np.linalg.norm(vector)
            magnitudes.append(magnitude)
    return magnitudes
 
# definiramo klasu koju ćemo koristiti pri određivanju vrste pravokutnika
class RectangleType:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_square(self):
        return self.width == self.height

# funkcija provjerava koju vrstu pravokutnika čine zadane točke
def determine_shape(points):
    magnitudes = vector_magnitudes(points)
    sorted_distances = sorted(magnitudes, reverse=True)
    width = sorted_distances[1]
    height = sorted_distances[2]

    shape = RectangleType(width, height)
    if shape.is_square():
            return "kvadrat"
    else:
            return "pravokutnik"

def main():
    file_path = "coordinates2D.txt"
    all_points = read_points(file_path)
    points = all_points[:-1]
    test_point = all_points[-1]

    if is_cuboid(points) == 1:
        print('- Zadane točke čine vrhove zajedničkog pravokutnika')
    else:
        print('- Zadane točke ne čine vrhove zajedničkog pravokutnika')
        quit()
    
    print("- Točka X nalazi se unutar pravokutnika" if is_point_inside(points, test_point) else "- Točka X ne nalazi se unutar pravokutnika")
    print(f"- Duljina dijagonale je {max(vector_magnitudes(points)):.2f}")
    print(f"- Zadane točke čine {determine_shape(points)}")
    
main()
