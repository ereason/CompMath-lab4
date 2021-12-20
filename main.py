import numpy as np
import spline
import buildPlot

# данные 1 варианта
Xn = np.array([1, 2, 3, 4, 5])
Fxn = np.array([4., 2., 8., 1., -1.])
# пример из текста задания
# Xn = np.array([0, 1, 2, 3, 4])
# Fxn = np.array([1., 3., 1., 4., 2.])
spline.Xn = Xn
spline.Fxn = Fxn
spline.segments = [[Xn[i], Xn[i + 1]] for i in range(len(Xn) - 1)]

# проверка на известных значениях
print([spline.approximate(Xn[i]) for i in range(len(Xn))])
# строим график
buildPlot.build(spline.approximate, spline.Xn)
