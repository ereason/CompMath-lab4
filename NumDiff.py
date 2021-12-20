import numpy as np

Xn = []
Fxn = []
segments = []


def h(a, b):
    return b - a


def dy(i):
    if i < 0 or i >= len(Xn):
        return undefined
    if i == 0:
        return (Fxn[i + 1] - Fxn[i]) / h(Xn[i], Xn[i + 1])
    if i == len(Xn) - 1:
        return (Fxn[i] - Fxn[i - 1]) / h(Xn[i - 1], Xn[i])

    return (Fxn[i + 1] - Fxn[i - 1]) / 2 * h(Xn[i - 1], Xn[i + 1])


def d2y(i):
    if i < 1 or i >= len(Xn) - 1:
        return undefined

    return (dy(i + 1) - dy(i - 1)) /  h(Xn[i - 1], Xn[i+1] )
