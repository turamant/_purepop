class CoordValue:
    '''
    класс Дескриптор
    '''
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if CoordValue.__checkValue(value):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError("Неверный формат данных")

    @staticmethod
    def __checkValue(a):
        if isinstance(a, int) or isinstance(a, float):
            return True
        return False

class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self,x=0,y=0):
        self.coordX = x
        self.coordY = y


'''
    @classmethod
    def coordinate_initial(cls):
        return cls(x=99,y=101)

    @staticmethod
    def __checkValue(a):
        if isinstance(a, int) or isinstance(a, float):
            return True
        return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, other):
        if  self.__checkValue(other):
            self.__x = other
        else:
            raise ValueError("Неверный формат данных - нужны цифры")

    @property
    def coordY(self):
        return self.__y

    @coordY.setter
    def coordY(self, other):
        if Point.__checkValue(other):
            self.__y = other
        else:
            raise ValueError("Неверный формат данных")

pt1 = Point(1,3)
#pt2 = Point.coordinate_initial()
#print('pt2-До этого было: ',pt2.coordX,pt2.coordY)
print('pt1-Было: ',pt1.coordX, pt1.coordY)
#pt2.coordX = 66
#pt2.coordY = 77
#print('pt2-Стало: ',pt2.coordX,pt2.coordY)
pt1.coordX = 99
pt1.coordY = 101
print('Стало: ',pt1.coordX,pt1.coordY)
'''

pt1 = Point(1,2)
print(pt1.coordX,pt1.coordY)
pt1.coordX = 1001
pt1.coordY = 2000

