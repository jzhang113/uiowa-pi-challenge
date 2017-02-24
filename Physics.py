#!/usr/bin/env python3
import Pool
import Processing

t = Processing.getTableState()

for ball in t.loc:
    print(str(ball.id) + " " + str(ball.x) + " " + str(ball.y))
