class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y



class B(A):
    slov = {}
    def __init__(self,z, *args):
        super().__init__(*args)
        slo
        self.z = z
    def display(self):
        print(self.x,self.y,self.z)

    def addSlovar(self):





a = A(12,13)
b = B(99,1,2)
b.display()