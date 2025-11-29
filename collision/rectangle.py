def isCorrectRect(coords):
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]
    
    return x2 > x1 and y2 > y1
    
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7,9), (3,6)]))