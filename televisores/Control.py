class Control:
     def __init__(self):
        self.tv=None 


     def enlazar(self,TV):
         self.tv=TV
         self.tv.setcontrol(self)


     def getTv(self):
        return self.tv

     def setTv(self,tv):
        self.tv=tv 



     def setCanal(self,canal):
         self.tv.Setcanal(canal)

     def turnOn(self):
        self.tv.turnOn()

     def turnOff(self):
        self.tv.turnOff()

    
     def volumenUp(self):
        self.tv.volumenUp()

     def volumenDown(self):
        self.tv.volumenDown() 

     def canalDown(self):
        self.tv.canalDown()    

     def canalUp(self):
        self.tv.canalUp()