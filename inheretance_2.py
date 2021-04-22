import math
from abc import ABCMeta, abstractmethod

class Fabric:
    fabric_list = {}
    def __init__(self, name, city, telephon, director):
        self.name = name
        self.city = city
        self.telephon = telephon
        self.director = director
        self.fabric_list[self.name] = {'фирма': self.name,
                                  'город':self.city,
                                  'телефон':self.telephon,
                                  'директор':self.director}

    def fabric_all(self):
        for k,v in self.fabric_list.items():
            print(k,':',v)

    def fabric_name(self):
        print(self.name)

class TabbleAbstract(metaclass=ABCMeta):
    __id = 0
    table_list = {}

    def __init__(self,  w=0, l=0, name='', model='', material='',color='',price=0.0):
        self.fabric = Fabric.fabric_list[name]
        self.width = w
        self.length = l
        self.model = model
        self.material = material
        self.color = color
        self.__price = price
        TabbleAbstract.__id += 1
        self.table_list[TabbleAbstract.__id] = {'фабрика': self.fabric,
                                                'ширина': self.width,
                                                'длинна': self.length,
                                                'модель': self.model,
                                                'материал': self.material,
                                                'цвет': self.color,
                                                'цена': self.__price,
                                                'площадь стола': self.area
                                                }


    def infoTable(self):
        print(f"Стол с параметрами:\n Фабрика: {self.fabric},\n ширина: {self.width}, длинна: {self.length} ,"
              f"модель: {self.model},\n Материал: {self.material}, Цвет: {self.color},"
              f"Цена стола: {self.__price}, Площадь стола: {self.area}" )


    def table_all(self):
        for k, v in self.table_list.items():
            print(k,':',v)

    def table_slice(self):
        for k, v in self.table_list.items():
            print(k,':',v['фабрика']['фирма'],v['цена'],'руб',v['площадь стола'],'mm')

    @staticmethod
    def getCountTable():
        return TabbleAbstract.__id

    @abstractmethod
    def area(self):
        pass


class RectTable(TabbleAbstract):
    @property
    def area(self):
        return self.width * self.length

class RouTable(TabbleAbstract):
    def __init__(self,radius=0.0, **kwargs):
        self.radius = radius
        super().__init__(**kwargs)

    @property
    def area(self):
        rad = self.radius * self.radius
        return round((math.pi * rad),2)

k = 'word'
if __name__=='__main__':
    while k != 'q':
        print('0 - record Fabric')
        print('1 - read Fabric')
        print('2 - record Table')
        print('3 - read Table')
        print('4 - read Slice Table')
        print('q - quit')
        k = input('Ваш выбор: ')
        print("Выбор равен: ",k)
        if k == '0':
            fabric1 = Fabric(input("Фирма: "), input('Город: '), input('Телефон: '), input('Диреkтор: '))
        if k == '1':
            fabric1.fabric_all()
        if k == '2':
            print('Произведем запись в БД стола')
            forma = input('1 - Круглый/ 2- прямоугольный?<1/2>: ')
            if forma == '2':
                shirina = int(input('Ширина: '))
                dlina = int(input('Длина: '))
                for k,_ in Fabric.fabric_list.items():
                    print(k)
                firma = input('Фирма: ')
                model = input('Модель: ')
                material = input('Материал:')
                color = input('Цвет: ')
                while 1:
                    try:
                        price = float(input('Цена: '))
                        break
                    except ValueError:
                        print('Ввводите цифры!!!')
                rt = RectTable(w=shirina, l=dlina, name=firma,model=model,
                               material=material, color=color, price=price)
            else:
                while 1:
                    try:
                        radius = float(input('Радиус: '))
                        break
                    except ValueError:
                        print('Ввводите цифры!!!')
                firma = input('Фирма: ')
                model = input('Модель: ')
                material = input('Материал:')
                color = input('Цвет: ')
                while 1:
                    try:
                        price = float(input('Цена: '))
                        break
                    except ValueError:
                        print('Ввводите цифры!!!')
                rt = RouTable(radius=radius,name=firma, model=model,material=material,
                                    color=color,price=price)
        if k == '3':
            print('Прочтем БД со столами')
            rt.infoTable()
            print('#'*25)
            rt.table_all()
            print('--==--'*12)
        if k == '4':
            print('Выборочные поля из БД со столами')
            print('--==--#' * 12)
            rt.table_slice()
            print('--==--' * 12)


