N, M = (5, 10)  # игровое поле NxN и число мин M

def createGame(PM):
    '''
    Создание игрового поля: раср=положение мин и
    подсчет числа мин вокруг клеток без мин
    :return:
    '''
    pass

def show():
    '''
    Функция отображения состояния текущего игрового поля
    :return:
    '''
    pass

def goPlayer():
    '''
    Функция для ввода пользователем координат
    закрытой клетки
    :return:
    '''
    pass

def isFinish():
    '''
    Функция опрделения текущего состояния игрыЖ
    выиграли , проиграли, игра продолжается
    :return:
    '''
    pass

def startGame():
    '''
    Функция запуска игры: отображается игровое поле,
    игрок открывает любую закрытую клетку,
    результат проверяется на наличие мины или выигрышной
    ситуации
    :return:
    '''
    P = [-2]*N*N
    PM = [0]*N*N
    createGame(PM)
    pass

if __name__=='__main__':
    startGame()
    while isFinish():
        show()
        goPlayer()
    print('GAME OVER')

