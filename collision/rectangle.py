class RectCorrectError(Exception):
    def __init__(self, index):
        super().__init__(f'{index}й прямоугольник некорректный')

class ValueError(Exception):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(f"Некорректный прямоугольник с координатами: x1 = {x1},  y1 = {y1}, x2 = {x2}, y2 = {y2}")

def isCorrectRect(rect):
    (x1, y1), (x2, y2) = rect    
    return x2 > x1 and y2 > y1
    
def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError(1)
    
    if not isCorrectRect(rect2):
        raise RectCorrectError(2)
    
    (x1, y1), (x2, y2) = rect1    
    (x3, y3), (x4, y4) = rect2    
    
    return not ((x2 <= x3 or x4 <= x1) or (y2 <= y3 or y4 <= y1))

def intersectionAreaRect(rect1, rect2):
    if not rect1 or not rect2:
        return 0
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    
    if not isCorrectRect(rect1):
        raise ValueError(x1, y1, x2, y2)
    
    if not isCorrectRect(rect2):
        raise ValueError(x3, y3, x4, y4)
    
    if not isCollisionRect(rect1, rect2):
        return 0
    
    x_left = max(x1, x3)
    x_right = min(x2, x4)
    
    y_bottom = max(y1, y3)
    y_top = min(y2, y4)
    
    return (x_right - x_left) * (y_top - y_bottom)

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0

    (x1, y1), (x2, y2) = rectangles[0]

    if not isCorrectRect(rectangles[0]):
        raise RectCorrectError(1)

    inter_left = x1
    inter_bottom = y1
    inter_right = x2
    inter_top = y2

    for i in range(1, len(rectangles)):
        rect = rectangles[i]
        if not isCorrectRect(rect):
            raise RectCorrectError(i+1)

        (rx1, ry1), (rx2, ry2) = rect

        inter_left = max(inter_left, rx1)
        inter_bottom = max(inter_bottom, ry1)
        inter_right = min(inter_right, rx2)
        inter_top = min(inter_top, ry2)

        if inter_left >= inter_right or inter_bottom >= inter_top:
            return 0

    return (inter_right - inter_left) * (inter_top - inter_bottom)
