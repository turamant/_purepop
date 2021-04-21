class Dog:
    __count = 0
    __instance = None

    def __init__(self,name="lkjhg", age=1, type="kjhgfd"):
        print("Cereate dog")
        self.name = name
        self.age = age
        self.type = type
        Dog.__count += 1

    @staticmethod
    def getCount():
        return Dog.__count

    def __new__(cls, *args, **kwargs):
        if (not isinstance(cls.__instance, cls)) or (Dog.__count < 5):
            cls.__instance = super(Dog, cls).__new__(cls)
            return cls.__instance
        else:
            print("Экземпляр уже создан")



class Rectangle:
    def __init__(self, h, w):
        self.__h = h
        self.__w = w
        self.square = Rectangle.__area(self.__h, self.__w)
        self.sq = self.__area(self.__h, self.__w)

    @staticmethod
    def __area(heigth, width):
        s = heigth * width
        return s

class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls ):
            cls.__instance = super(Point, cls).__new__(cls)
            return cls.__instance
        else:
            print("Экземпляр уже создан")

    def __init__(self, x=0,y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod
    def getCount():
        return Point.__count

pt = Point(1,2)
pt2 = Point(4,5)
pt3 = Point(6,7)
print(id(pt),id(pt2),id(pt3))
print(pt.coordY)

print("================")
rt1 = Rectangle(2,3)
print(rt1.square)
print(rt1.sq)


for i in range(10):
    dog = Dog()
    print(id(dog))
print("Всего создано собак: ",Dog.getCount())



