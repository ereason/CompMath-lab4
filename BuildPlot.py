import matplotlib.pyplot as plt
import numpy as np


def axisSetUp():
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))


def build(f, Xn):
    axisSetUp()

    x = np.arange(Xn[0], Xn[-1], 0.1)
    y = [f(x[i]) for i in range(len(x))]
    plt.plot(x, y)

    pointsY = [f(Xn[i]) for i in range(len(Xn))]
    for i_x, i_y in zip(Xn, pointsY):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()
