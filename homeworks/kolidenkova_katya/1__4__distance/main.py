from math import sqrt
f = open('text4')

def distance(point1,point2):
    x = abs(float(point1[0]) - float(point2[0]))
    y = abs(float(point1[1]) - float(point2[1]))
    return(sqrt(x**2+ y**2))

try:
    points = []
    for line in f:
        point = line.strip()
        points.append(point.split(" "))

    max = distance(points[0], points[1])
    min = distance(points[0], points[1])

    for i in range(0, len(points)):
        for j in range(i+1,len(points)):
            if max < distance(points[i], points[j]):
                max = distance(points[i], points[j])
            if min > distance(points[i], points[j]):
                min = distance(points[i], points[j])

    print("max = ", max)
    print("min = ", min)

except IndexError:
    print("Incorrect data!")
except ValueError:
    print("Incorrect data! Erase all blank lines and make sure that all lines contain nothing but numbers!")
