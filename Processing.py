#!/usr/bin/env python3
from Pool import *

def getTableState():
    # get real values from image data
    width = 100
    length = 200
    balls = []
    for x in range(15):
        balls.append(Ball(5 * x, 5 * x, x))

    return Table(width, length, balls)
