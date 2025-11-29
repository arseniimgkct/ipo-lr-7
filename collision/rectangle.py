class RectCorrectError(Exception):
    def __init__(self):
        super().__init__("Некорректный прямоугольник")

class ValueError(Exception):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(f"Некорректный прямоугольник с координатами: x1 = {x1},  y1 = {y1}, x2 = {x2}, y2 = {y2}")

def isCorrectRect(rect):
    (x1, y1), (x2, y2) = rect    
    return x2 > x1 and y2 > y1
    
def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError()
    
    if not isCorrectRect(rect2):
        raise RectCorrectError()
    
    (x1, y1), (x2, y2) = rect1    
    (x3, y3), (x4, y4) = rect2    
    
    return not ((x2 <= x3 or x4 <= x1) or (y2 <= y3 or y4 <= y1))

def intersectionAreaRect(rect1, rect2):
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    
    if not isCorrectRect(rect1):
        raise ValueError(x1, y1, x2, y2)
    
    if not isCorrectRect(rect2):
        raise ValueError(x3, y3, x3, y4)
    
    if not isCollisionRect(rect1, rect2):
        return 0
    
    x_left = max(x1, x3)
    x_right = min(x2, x4)
    
    y_bottom = max(y1, y3)
    y_top = min(y2, y4)
    
    return (x_right - x_left) * (y_top - y_bottom)