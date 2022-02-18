from abc import ABCMeta, abstractmethod
import logging

logging.basicConfig(filename = 'log_es_persona.log' ,format=' %(levelname)s %(asctime) s %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Persona(metaclass=ABCMeta):
    def __init__(self,nome, cognome, data_nascita, sesso, peso):
        self._nome=nome
        self._cognome=cognome
        self._data_nascita=data_nascita
        self._sesso=sesso
        self._peso=peso
        
    #getter 
    def get_name(self):
        return self._nome 


    # getter 
    def get_cognome(self):
        return self._cognome
    
    # getter 
    def get_data_nscita(self):
        return self._data_nascita
    
    # getter 
    def get_sesso(self):
        return self._sesso
    
    # getter 
    def get_peso(self):
        return self._peso
    
    def mangia(self):
        print('la persona sta mangiando')

    def cammina(self):
        print('la persona sta camminando')
        
    def dorme(self):
        print('la persona sta dormendo')  
        
    def __str__(self):
        return str(self._nome) + ' ' + str(self._cognome) + ' ' + str(self._data_nascita) + ' ' + str(self._sesso) + str(self._peso)
    
    def __eq__(self,other):
            if other._nome==self._nome and other._cognome==self._cognome and other._data_nascita==self._data_nascita and other._sesso==self._sesso and other._peso==self._peso:
                return True
            return False 


class Lavoratore(Persona, metaclass=ABCMeta):
    
    def __init__(self,nome, cognome, data_nascita, sesso, peso, idbadge, mansione):
        super().__init__(nome, cognome, data_nascita, sesso, peso)
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
    
    
from persona import Persona
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Studente(Persona):

    @property
    def matricola(self):
        return  self._matricola

    @matricola.setter
    def matricola(self, matricola):
        self._matricola = matricola

    @property
    def corso_di_studio(self):
        return self._corso_di_studio

    @corso_di_studio.setter
    def corso_di_studio(self, corso_di_sudtio):
        self._corso_di_studio = corso_di_sudtio

    @property
    def alchool(self):
        return self._alchool

    @alchool.setter
    def alchool(self, alchool):
        self._alchool = alchool

    @alchool.deleter
    def alchool(self):
        self._alchool = list()

    @property
    def esami(self):
        return self._esami

    @esami.setter
    def esami(self, esami):
        self._esami = esami

    def __init__(self, nome: str, cognome: str, sesso: bool, peso: int, data_di_nascita: datetime, matricola: int,
                 corso_di_studio: str, alchool: list, esami: dict):
        """
        Metodo init per la creazione di uno studente
        :param nome: nome dello studente, deve essere di tipo str.
        :param cognome: cognome dello studente, deve essere di tipo str.
        :param sesso: sesso dello studente, deve essere True per maschio False per le femmina.
        :param peso: peso dello studente, deve essere un intero.
        :param data_di_nascita: data di nascita dello studente, deve essere di tipo datetime.
        :param matricola: matricola dello studente, deve essere un intero.
        :param corso_di_studio: cordo di studio dello studente, deve essere una stringa.
        :param alchool: lista di bevande consumate dallo studente, deve essere una lista di tuple di lunghezza due, al
        primo posto il tasso alcholico della bevanda e al secondo il volume della bevanda e.g. [(14, 200), (30, 50)]
        si nota che il primo membro della tupla e` una percentuale quiindi i valori devono essere compresi tra 0 e 100.
        :param esami: dizionario degli esami conseguiti dallo studente, il dizionario deve avere come chiave il nome
        dell'esame e come valore la tupla (crediti, voto, lode), dove crediti e voto sono interi e il voto deve essere
        compreso tra 18 e 30, mentre lode e` un boolean, si nota che la lode non puo` essere assegnata se il voto non
        e` 30.
        """

        for e in esami.values():
            assert isinstance(e, tuple)
            assert len(e) == 3
            assert isinstance(e[0], int) and isinstance(e[1], int) and isinstance(e[2], bool)
            assert 18 <= e[1] <= 30
            assert e[1] != 30 and e[3] is True
        assert isinstance(nome, str)
        assert isinstance(cognome, str)
        assert isinstance(data_di_nascita, datetime)
        for a in alchool:
            assert isinstance(a, tuple)
            assert len(a) == 2
            assert 0 <= a[0] <= 100

        super().__init__(nome, cognome, data_di_nascita, sesso, peso)
        self._matricola = matricola
        self._corso_di_studio = corso_di_studio
        self._alchool = alchool
        self._esami = esami

    def __eq__(self, other):
        """
        funziona equal che paragona se due studenti sono uguali usando il numero matricola.
        :param other: oggetto di tipo persona
        :return: True se i due oggetti Studente hanno la stessa matricola altrimenti False.
        """
        return True if self._matricola == other.matricola else False

    def __str__(self):
        return str(f"Studente {self._nome} {self._cognome}, matricola {self._matricola}, iscritto al corso di studio"
                   f"{self._corso_di_studio}")

    def calcolo_media_esami(self):
        """
        metodo che calcola la media degli esami.
        :return: ritorna la media degli esami.
        """
        crediti_totali = sum(map(lambda x: x[0], self._esami.values()))
        media = sum(map(lambda x: x[0] * x[1], self._esami.values())) / crediti_totali
        return media

    def calcola_tasso_alcolemico(self):
        """
        metodo che calcola il tasso alcolemico.
        :return: ritornoa il tasso alcolemico.
        """
        coefficente_difusione = 0.73 if self._sesso else 0.66
        sum_beverage = sum(map(lambda x: x[0] * x[1], self._alchool))
        return sum_beverage * 0.008 * 1.055 / (coefficente_difusione * self._peso)


from persona import Lavoratore


class LavoratorePiva(Lavoratore):
    def __init__(self,nome, cognome, data_nascita, sesso, peso, idbadge, mansione,tariffa_gg, ore_lavorate):
        super().__init__(nome, cognome, data_nascita, sesso, peso, idbadge, mansione, tariffa_gg, ore_lavorate)
        self._tariffa_gg=tariffa_gg
        self._ore_lavorate=ore_lavorate
        logger.info("E' stato inserito un lavoratore con P.iva.")  

          

        
    def __str__(self):
        return super().__str__() + ' ' + self._tariffa_gg + ' ' + self._ore_lavorate
    
    def __eq__(self, other):
        if isinstance(other, LavoratorePiva):
            if super().__eq__(other) and other._tariffa_gg == self._tariffa_gg and other._ore_lavorate == self._ore_lavorate:
                return True
        return False
    
    def get_tariffa_gg (self):
        return self.get_tariffa_gg
    
    def set_tariffa_gg (self,x):
        if x<=0:
            raise ('Tariffa non valida!')
        else:
            self._tariffa_gg=x
            
    def get_ore_lavorate(self):
        return self.get_ore_lavorate
    
    def set_ore_lavorate(self,x):
        if x<0:
            raise ('Ore lavorate non può essere negativo!')
        elif x==0:
            raise ('Nessuna ora di lavoro')
        else:
            self._ore_lavorate=x
                 
    
    
    def calcola_stipendio(self):
        stipendio= sum(map(lambda x: x[0] + x[1], self._tariffa_gg.values(),self._ore_lavorate.values())) 
        return stipendio 
        
