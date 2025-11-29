from collision import isCorrectRect, isCollisionRect

print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7,9), (3,6)]))

print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))
print(isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]))
print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]))