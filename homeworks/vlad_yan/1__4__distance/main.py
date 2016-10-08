import math
from optparse import OptionParser
from collections import namedtuple

point = namedtuple('Point', 'x, y')


def dist(a, b):
    """Calculate distance between two points: a and b."""
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def mycartesian_product(some_list):
    """Get cartesian product of a list with itself."""
    pr = []
    for ind, item1 in enumerate(some_list[:-1], start=1):
        for item2 in some_list[ind:]:
            pr.append((item1, item2))

    return pr


def xy_from_file(filename):
    """Read in point coordinates from a given file."""
    with open(filename) as fobj:
        content = fobj.readlines()

    try:
        splited = [line.split() for line in content]
        points = [point(float(x), float(y)) for x, y in splited]
    except ValueError:
        return None

    return points


def main(filename):
    """Main function."""
    points = xy_from_file(filename)
    cartesian_prod = mycartesian_product(points)
    distances = [dist(p1, p2) for p1, p2 in cartesian_prod]

    min_ = min(distances)
    max_ = max(distances)

    print('min: %s\nmax: %s' % (min_, max_))


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()

    arg = args[0]
    main(arg)
