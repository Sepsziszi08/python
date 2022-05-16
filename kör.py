import math

class kör:
    def __init__(self,x,y,r):
        self.x=x
        self.y=x
        self.r=r


    def nagyít(self, mennyivel=1):
        self.r+=mennyivel

    def kicsinyít(self, mennyivel=1):
        self.r-=mennyivel



    def kerület(self):
        return 2*self.r*math.pi

    def terület(self):
        return self.r**2*math.pi/2

k=kör(0,0,10)
print(k.r)
k.nagyít()
print(k.r)
k.nagyít(100)
print(k.r)
k.kicsinyít(100)
print(k.r)
print(k.kerület())
print(k.terület())
