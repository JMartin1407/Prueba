
class Tinaco:
    def __init__(self, capLts, contLts):
        self.capLts = capLts
        self.contLts = contLts

    def llenar (self, litros):
        if self.contLts + litros > self.capLts:
            print('Se llego a la capacidad máxima')
            self.contLts = self.capLts
        else:
            self.contLts += litros
        return self.contLts
    
    def vaciar(self, litros):
        if litros >= self.contLts:
            print('El tinaco se vacio por completo')
            self.contLts = 0
        else:
            self.contLts -=litros
        return self.contLts
    
    def __str__(self):
        return f'Capacidad del tinaco: {self.capLts} litros, Contenido actual: {self.contLts} litros'