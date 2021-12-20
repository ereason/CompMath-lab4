import numpy as np
import Spline
import NumDiff
import BuildPlot
import math

# данные 1 варианта
Xn = np.array([1, 2, 3, 4, 5])
Fxn = np.array([4., 2., 8., 1., -1.])
# пример из текста задания
# Xn = np.array([0, 1, 2, 3, 4])
# Fxn = np.array([1., 3., 1., 4., 2.])
Spline.Xn = Xn
Spline.Fxn = Fxn
Spline.segments = [[Xn[i], Xn[i + 1]] for i in range(len(Xn) - 1)]

testXn = [-0.0001, 0, 0.0001]
testYn = [math.cos(testXn[0]), math.cos(testXn[1]), math.cos(testXn[2])]
NumDiff.Xn = testXn
NumDiff.Fxn = testYn
print(NumDiff.d2y(1))

# проверка на известных значениях
print([Spline.approximate(Xn[i]) for i in range(len(Xn))])
# строим график
BuildPlot.build(Spline.approximate, Spline.Xn)
