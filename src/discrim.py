def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    d = b ** 2 - 4 * a * c
    #print(d)
    return d

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    list1 = []
    d = discriminant(a, b, c)
    if d < 0:
        return list1
    elif d == 0:
        list1.append(-b / (2 * a))
        return list1
    elif d > 0:
        list1.append((-b + d ** (1 / 2)) / (2 * a))
        list1.append((-b - d ** (1 / 2)) / (2 * a))
        #print(list1)
        return list1


