from abc import ABCMeta, abstractmethod


from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    def __init__(self,nome, cognome, data_nascita):
        self._nome=nome
        self._cognome=cognome
        self._data_nascita=data_nascita
        
    #getter 
    def get_name(self):
        return self._nome 


    # getter 
    def get_cognome(self):
        return self._cognome
    
     # getter 
    def get_data_nscita(self):
        return self._data_nascita
    
    
    def mangia(self):
        print('la persona sta mangiando')

    def cammina(self):
        print('la persona sta camminando')
        
    def dorme(self):
        print('la persona sta dormendo')    