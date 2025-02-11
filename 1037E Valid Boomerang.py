def isBoomerang(points):
    for i in points:
        if i[0] != i[1]:
            x = True
            return x
        return False

p = [[0,0],[2,1],[2,1]]
print(isBoomerang(p))

"""Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line."""