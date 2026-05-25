class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i} + {self.j}")

class ThreeDvector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i} + {self.j} + {self.k}")

a = TwoDVector(2,3)
a.show()
b = ThreeDvector(4,5,6)
b.show()



