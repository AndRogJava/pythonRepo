from abc import ABCMeta, abstractmethod
import logging

logging.basicConfig(filename = 'log_es_persona.log' ,format=' %(levelname)s %(asctime) s %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
        
    def __str__(self):
        return str(self._nome) + ' ' + str(self._cognome) + ' ' + str(self._data_nascita) 
    
    def __eq__(self,other):
        if isinstance(other):
            if other._nome==self._nome and other._cognome==self._cognome and other._data_nascita==self._data_nascita:
                return True
            return False 


class Lavoratore(Persona, metaclass=ABCMeta):
    
    def __init__(self,nome, cognome, data_nascita, idbadge, mansione):
        super().__init__(nome, cognome, data_nascita)
        Lavoratore.check_id(idbadge)
        self._idbadge = idbadge
        self._mansione = mansione
        logger.info("E' stato inserito un lavoratore.")  
    
    def __str__(self):
        return super().__str__() + ' ' + self._idbadge + ' ' + self._mansione

    def __eq__(self, other):
        if isinstance(other, Lavoratore):
            if super().__eq__(other) and other._idbadge == self._idbadge and other._mansione == self._mansione:
                return True
        return False
    
    def __hash__(self):
        return hash((super().__hash__(), self._idbadge, self._mansione))

    def get_idbadge(self):
        return self._idbadge

    def set_idbadge(self, x):
        Lavoratore.check_id(x)
        self._idbadge = x
    
    def get_masnione(self):
        return self._mansione
    
    def set_mansione(self, x):
        if(len(x)<0) or (x.isalpha() == False):
            raise('Inserisci una mansione valida')
        else:
            self._mansione = x
    
    @staticmethod
    def check_id(idbadge):
        if (len(idbadge)<0) or (len(idbadge)>8) or (idbadge.isalnum() == False):
            raise('Inserisci una id valido.')
        else:
            pass


    @abstractmethod
    def stipendio(self):
        pass