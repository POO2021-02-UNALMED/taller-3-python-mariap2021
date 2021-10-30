class TV:
    numTV=0
    def __init__(self,marca,estado):
         self.marca =marca
         self.estado=estado
         self.canal=1
         self.precio=500
         self.volumen=1
         self.control=None
         
         TV.numTV+=1
	     

    
    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca=marca

    
    
    def getPrecio(self):
        return self.precio

    def setPrecio(self,precio):
        self.precio=precio
        
        

    def getCanal(self):
        return self.canal 
	
    def setCanal(self, canal):
        if(self.estado==False): 
            return
            if(canal>=1 and canal <=120):
                self.canal=canal
		
    def getCanal(self):
        return self.canal


    def getEstado(self):
        return self.estado   

    @classmethod            
    def getNumTV(cls):
        return cls.numTV

    @classmethod            
    def setNumTV(cls,numTv):
        cls.numTV=numTv 



    def getControl(self):
        return self.control

    def setControl(self,control):
        self.control=control

    def getVolumen(self):
        return self.volumen 

    def setVolumen(self, volumen):
        if(self.estado==False): 
            return
            if(volumen>=0 and volumen <=7):
                self.volumen=volumen    

    def volumenUp(self):
        if(self.estado==False and self.volumen==7): 
            return
        else:
            self.volumen=self.volumen+1    
