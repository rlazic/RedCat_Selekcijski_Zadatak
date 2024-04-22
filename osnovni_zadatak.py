import math

#učitavamo koordinata iz datoteke
def load_file(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            coordinates = [list(map(float, line.strip().split(', '))) for line in lines]
        return coordinates


#računamo udaljenosti između dvije točke
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

#provjeravamo jesu li učitane točke A, B i C vrhovi pravokutnika
def is_rectangle(A, B, C):

    AB = distance(A, B)
    BC = distance(B, C)
    AC = distance(A, C)

    #provjeravamo jesu li učitane točke vrhovi jednakostraničnog trokuta. Ukoliko jesu, program se zaustavlja    
    if AB == AC == BC:
        return False

    #definiramo najdulju stranicu zadanog trokuta, zatim preko pitagorinog poučka računamo "fiktivnu" dijagonalu     
    longest_distance = max(AB, BC, AC)
    
    if longest_distance == AB:
        diagonal = math.sqrt(AC**2 + BC**2)
    elif longest_distance == BC:
        diagonal = math.sqrt(AB**2 + AC**2)
    else:
        diagonal = math.sqrt(AB**2 + BC**2)

    #uspoređujemo najdulju stranicu trokuta sa fiktivnom dijagonalom. Ukoliko su vrijednosti jednake, zadane točke čine vrhove pravokutnika    
    if longest_distance == diagonal:
        return True
    else:
        return False

#provjeravamo nalazi li se točka X unutar zadanog pravokutnika
def is_inside_rectangle(A, B, C, X):

    #određujemo granice pravokutnika
    min_x = min(A[0], B[0], C[0])
    max_x = max(A[0], B[0], C[0])
    min_y = min(A[1], B[1], C[1])
    max_y = max(A[1], B[1], C[1])
    
    if min_x <= X[0] <= max_x and min_y <= X[1] <= max_y:
        return True
    else:
        return False

#računamo duljinu dijagonale
def diagonal_length(A, B, C):
    AB = distance(A, B)
    BC = distance(B, C)
    AC = distance(A, C)
    return max(AB, BC, AC)

#izvršavamo definirane funkcije
def main():
    filename = "coordinates.txt"
    coordinates = load_file(filename)
    
    A, B, C, X = coordinates
    
    if not is_rectangle(A, B, C):
        print("Točke A, B i C nisu vrhovi istog pravokutnika.")
        exit()
    if is_rectangle(A, B, C):
        print("Točke A, B i C su vrhovi istog pravokutnika.")

    if is_inside_rectangle(A, B, C, X):
        print("Točka X se nalazi unutar pravokutnika.")
    else:
        print("Točka X se ne nalazi unutar pravokutnika.")
    
    d_length = diagonal_length(A, B, C)
    print(f"Dijagonala pravokutnika je dugačka: {d_length:.1f}")

if __name__ == "__main__":
    main()
