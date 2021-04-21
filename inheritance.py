class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Prop:
    def __init__(self, sp:Point,ep:Point, color:str="red", width:int=1):
        print("Конструктор базового класса Prop")
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width

class Line(Prop):
    def __init__(self,*args):
        print("переопрделеный конструктор Line")
        #Prop.__init__(self, *args)
        #super(Line, self).__init__(*args)
        super().__init__(*args)

    def drawLine(self):
        print(f'Рисование линии {self._sp}, {self._ep}, {self._color},{self.getWidth()}')

class Rectangle(Prop):
    def __init__(self, *args):
        super(Rectangle, self).__init__(*args)

    def drawRectangle(self):
        print(f'рисование прямоугольника {self._sp}, {self._ep}, {self._color},{self._Prop__width} ')


class PersonalComputer:
    def __init__(self, ddr, hdd, model, cpu):
        self.ddr = ddr
        self.hdd = hdd
        self.model = model
        self.cpu = cpu


class DesktopPC(PersonalComputer):
    infoPC = {}
    def __init__(self, monitor, keyboard, mouse, size, *args):
        super().__init__(*args)
        self.infoPC['Монитор'] = monitor
        self.infoPC['Клавиатура'] = keyboard
        self.infoPC['Мышка'] = mouse
        self.infoPC['Габариты'] = size
        self.infoPC['Память'] = args[0]
        self.infoPC['Жесткий диск'] = args[1]
        self.infoPC['Модель'] = args[2]
        self.infoPC['ЦПУ'] = args[3]

    def getInfoPC(self):
        print('< DeskTopPc info >')
        for k, v in DesktopPC.infoPC.items():
            print(k, ':', v)
class NoteBook(PersonalComputer):
    InfoNoteBook = {}
    def __init__(self, size, diagonal, *args):
        super().__init__(*args)
        self.InfoNoteBook['Габариты'] = size
        self.InfoNoteBook['Диагональ'] = diagonal
        self.InfoNoteBook['Паямять'] = args[0]
        self.InfoNoteBook['Жесткий диск'] = args[1]
        self.InfoNoteBook['Модель'] = args[2]
        self.InfoNoteBook['ЦПУ'] =args[3]

    def getInfoNoteBook(self):
        print('< NoteBook info >')
        for k, v in NoteBook.InfoNoteBook.items():
            print(k, ':', v)


pc = DesktopPC('Soni`17','key101','genius','127x123x78',256,'1Tb','iCore7','Intel Pentium',)
pc.getInfoPC()
print(25 * '-')
pc2 = DesktopPC('Samsung`19','key101-1','DEXP','134x544x78',512,'2Tb','iCore5','AMD Risen',)
pc.getInfoPC()
print(25 * '-')
nb = NoteBook('123x34,456','`15.2',512,'2Tb','iCore5','AMD Risen')
nb.getInfoNoteBook()


l = Line(Point(1,2), Point(10,20))
l.drawLine()
r = Rectangle(Point(34,34),Point(3,8))
r.drawRectangle()


