import numpy as np
from scipy import interpolate
import buildPlot

# данные 1 варианта
Xn = np.array([1, 2, 3, 4, 5])
Fxn = np.array([4., 2., 8., 1., -1.])

#Xn = np.array([0, 1, 2, 3, 4])
#Fxn = np.array([1., 3., 1., 4., 2.])
otrezoki = [[Xn[i],Xn[i+1]] for i in range(len(Xn)-1)]

def calculateA(Fx):
    return [Fxn[i] for i in range(len(Fx)-1)]

def calculateC(h,n):
    A = np.array([[4*h if y==x  else
                   h if x+1==y or x-1 == y
                   else 0 for x in range(n)] for y in range(n)])

    b = np.array([(3/h) * (Fxn[2+i] -2*Fxn[1+i] + Fxn[i]) for i in range(0,n)])

    return np.concatenate((np.array([0]), np.linalg.solve(A,b)))

def calculateD(c,otrezki):
    d = []
    for i in range(len(otrezki)):
        if i == len(otrezki)-1:
            d.append( (0 - c[i]) / (3 * h(otrezki[i])))
            continue
        d.append( (c[i+1] - c[i]) / (3 * h(otrezki[i])))
    return d

def calculateB(a,c,Fxn,otrezki):
    b = []
    for i in range(len(otrezki)):
        if i == len(otrezki) - 1:
            part1 = (Fxn[i+1] - Fxn[i]) / (h(otrezki[i]))
            part2 = ((0 + 2.0*c[i]) * (h(otrezki[i]))) / 3.0
            b.append(part1 - part2)
            continue

        part1 = (a[i+1] - a[i] ) / ( h(otrezki[i]))
        part2 = ((c[i+1] + 2.0*c[i]) * ( h(otrezki[i])) ) / 3.0
        b.append( part1 - part2 )

    return b


def h(range):
    return range[1]-range[0]

def func(x):
    a = calculateA(Fxn)
    c = calculateC(h(otrezoki[0]), len(otrezoki)-1)
    d = calculateD(c,otrezoki)
    b = calculateB(a,c,Fxn,otrezoki)

    i = -1
    k = otrezoki[0][0]
    for j in range(len(otrezoki)):
        if  otrezoki[j][0] <= x and x < otrezoki[j][1]:
            k = otrezoki[j][0]
            i = j
            break

    if x == otrezoki[-1][1]:
        i = len(otrezoki)-1
        k = otrezoki[-1][0]

    return a[i] + b[i]*(x-k) + c[i]*(x-k)*(x-k) + d[i]*(x-k)*(x-k)*(x-k)




print([func(Xn[i]) for i in range(len(Xn))])
buildPlot.build(func,Xn)


