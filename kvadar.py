import numpy as np

# funkcija učitava točke iz datoteke
def read_points(file_path):
    with open(file_path, 'r') as file:
        all_points = [np.fromstring(line.strip(), sep=',') for line in file]
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

# funkcija provjerava nalazi li se zadana točka unutar kvadra
def is_point_inside(points, test_point):  
    min_bound = np.min(points, axis=0)
    max_bound = np.max(points, axis=0)
    return np.all(min_bound <= test_point) and np.all(test_point <= max_bound)

# funkcija računa duljinu prostorne dijagonale
def spatial_diagonal(points):
    for i in range(4):
        # definiramo referentnu točku
        ref_point = points[i]
        vectors = [np.array(points[j]) - np.array(ref_point) for j in range(4) if j != i]
        # provjeravamo jesu li sva tri vektora iz referentne točke međusobno okomiti
        if np.dot(vectors[0], vectors[1]) == 0 and np.dot(vectors[0], vectors[2]) == 0 and np.dot(vectors[1], vectors[2]) == 0:
            dimensions = [np.linalg.norm(v) for v in vectors]
            # računamo prostornu dijagonalu pomoću Pitagorinog poučka
            x, y, z = dimensions
            diagonal = np.sqrt(x**2 + y**2 + z**2)
            return diagonal

        else:
            # definiramo prostornu dijagonalu kao najveću duljinu između zadanih točaka
            max_magnitude = 0
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                        vector = points[i] - points[j]
                        vec_magnitude = np.linalg.norm(vector)
                        if vec_magnitude > max_magnitude:
                            max_magnitude = vec_magnitude
            return max_magnitude

def main():
    file_path = "koordinate3D.txt"
    all_points = read_points(file_path)
    points = all_points[:-1]
    test_point = all_points[-1] 

    if is_cuboid(points) in (3,4):
        print('- Zadane točke čine vrhove zajedničkog kvadra')
    else:
        print('- Zadane točke ne čine vrhove zajedničkog kvadra')
        quit()
    
    print("- Točka X nalazi se unutar kvadra" if is_point_inside(points, test_point) else "Točka X ne nalazi se unutar kvadra")
    print(f"- Duljina prostorne dijagonale je {spatial_diagonal(points):.2f}")
    
main()

