
def read_file(file_name):
    coords_file = open(file_name, 'r')
    coords = []
    for line in coords_file:
        coords.append([float(s) for s in line.split()])
    return coords


def distance(coord1, coord2):
    return ((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)**0.5


def get_min_distance(coords):
    current_position = 0
    min_distance = distance(coords[0], coords[1])
    for i in range(0, len(coords)-1):
        for j in (current_position+1, len(coords)-1):
            if min_distance > distance(coords[i], coords[j]):
                min_distance = distance(coords[i], coords[j])
        current_position += 1
    return min_distance


def get_max_distance(coords):
    current_position = 0
    max_distance = distance(coords[0], coords[1])
    for i in range(0, len(coords)-1):
        for j in (current_position+1, len(coords)-1):
            if max_distance < distance(coords[i], coords[j]):
                max_distance = distance(coords[i], coords[j])
        current_position += 1
    return max_distance


coords_file_name = "coords.txt"
my_coords = read_file(coords_file_name)
print("Наименьшее расстояние между точками: ", get_min_distance(my_coords))
print("Наибольшее расстояние между точками: ", get_max_distance(my_coords))
