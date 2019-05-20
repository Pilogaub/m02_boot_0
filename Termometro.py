class Termometro():
    def __init__(self):
        self.__unidadM = "ºC"
        self.__temperatura = 0
    
    def __conversor(self, temperatura, unidad):
        if unidad == "ºC":
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{}º C".format((temperatura - 32)*5/9)
        else:
            return "unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidadM)
    
    def unidadMedida(self, uniM=None): #es el getter y el setter de la unidad de medida
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "ºC":
                self.__unidadM = uniM
    
    def temp(self, temperatura=None): #es el getter y el setter de la temperatura
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
    
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == "F" or uniM == "C":
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()