class RectCorrectError(Exception):
    def __init__(self):
        super().__init__("Некорректный прямоугольник")

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