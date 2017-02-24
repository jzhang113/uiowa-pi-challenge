#!/usr/bin/env python3

class Ball:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        
    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def moveAngle(self, f, t):
        self.x += f * math.cos(t)
        self.y += f * math.sin(t)

class Table:
    def __init__(self, w, l, balls):
        self.width = w
        self.length = l
        self.loc = balls
