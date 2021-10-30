class Control:
     def __init__(self):
        self.tv=None 


     def enlazar(self,tv):
         self.tv=tv
         self.tv.setControl(self)


     def getTv(self):
        return self.tv

     def setTv(self,tv):
        self.enlazar=tv 

     def setCanal(self,canal):
         self.tv.setCanal(canal)

     def turnOn(self):
        self.tv.turnOn()

     def turnOff(self):
        self.tv.turnOff()

     def setControl(self,control):
        self.tv.setControl()   

    
     def volumenUp(self):
        self.tv.volumenUp()

     def volumenDown(self):
        self.tv.volumenDown() 

     def canalDown(self):
        self.tv.canalDown()    

     def canalUp(self):
        self.tv.canalUp()    



     

