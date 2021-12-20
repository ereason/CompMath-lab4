import numpy as np

Xn = []
Fxn = []
segments = []


def calculateA(Fx):
    return [Fxn[i] for i in range(len(Fx) - 1)]


def calculateC():
    n = len(segments) - 1
    A = np.array([[4 * h(segments[y]) if y == x else
                   h(segments[x]) if x + 1 == y or x - 1 == y
                   else 0 for x in range(n)] for y in range(n)])

    b = np.array([(3 / h(segments[i])) * (Fxn[2 + i] - 2 * Fxn[1 + i] + Fxn[i]) for i in range(0, n)])

    return np.concatenate((np.array([0]), np.linalg.solve(A, b)))


def calculateD(c):
    d = []
    for i in range(len(segments)):
        if i == len(segments) - 1:
            d.append((0 - c[i]) / (3 * h(segments[i])))
            continue
        d.append((c[i + 1] - c[i]) / (3 * h(segments[i])))
    return d


def calculateB(a, c):
    b = []
    for i in range(len(segments)):
        if i == len(segments) - 1:
            part1 = (Fxn[i + 1] - Fxn[i]) / (h(segments[i]))
            part2 = ((0 + 2.0 * c[i]) * (h(segments[i]))) / 3.0
            b.append(part1 - part2)
            continue
        part1 = (a[i + 1] - a[i]) / (h(segments[i]))
        part2 = ((c[i + 1] + 2.0 * c[i]) * (h(segments[i]))) / 3.0
        b.append(part1 - part2)
    return b


def h(range):
    return range[1] - range[0]


def approximate(x):
    a = calculateA(Fxn)
    c = calculateC()
    d = calculateD(c)
    b = calculateB(a, c)

    i = -1
    k = segments[0][0]
    for j in range(len(segments)):
        if segments[j][0] <= x and x < segments[j][1]:
            k = segments[j][0]
            i = j
            break

    if x == segments[-1][1]:
        i = len(segments) - 1
        k = segments[-1][0]

    return a[i] + b[i] * (x - k) + c[i] * (x - k) * (x - k) + d[i] * (x - k) * (x - k) * (x - k)
