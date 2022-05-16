# part A

def slope(x1, y1, x2, y2):
    m = ((y2-y1)/(x2-x1))
    return m

def report(x1, y1, x2, y2):
    point1 = x1, y1 
    point2 = x2, y2
    return point1, point2

slopeFromPoints = slope(3, 4, 9, 10)
points = report(3, 4, 9, 10)
print(f"the slope of the line colinear with points {points} is {slopeFromPoints}")
