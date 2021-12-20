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


def build(f):
    axisSetUp()

    t1 = np.arange(-10, 10, 0.1)
    plt.plot(t1, f(t1))

    plt.show()
