from abc import ABCMeta, abstractmethod
import logging
from datetime import datetime


logging.basicConfig(filename = 'log_es_persona.log' ,format=' %(levelname)s %(asctime) s %(message)s',level=logging.DEBUG)
logger = logging.getLogger(__name__)

stipendi = {
    "addetto_pulizia": {
        1: 2000,
        2: 1800,
        3: 1700,
        4: 1500,
        5: 1400,
        6: 1300,
        7: 1200
    },
    "inserviente": {
        1: 2050,
        2: 1850,
        3: 1750,
        4: 1550,
        5: 1450,
        6: 1350,
        7: 1250
    },
    "operaio": {
        1: 2500,
        2: 2300,
        3: 2000,
        4: 1900,
        5: 1800,
        6: 1500,
        7: 1400
    },
    "fattorino": {
        1: 2500,
        2: 2300,
        3: 2000,
        4: 1900,
        5: 1800,
        6: 1500,
        7: 1400
    },
    "Manager": {
        1: 4000,
        2: 3700,
        3: 3500,
        4: 3300,
        5: 3000,
        6: 2800,
        7: 2500
    },
    "Driettore": {
        1: 7000,
        2: 6500,
        3: 6200,
        4: 6000,
        5: 5800,
        6: 5500,
        7: 5000
    }

}


class LevelError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MansioneError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class IllegalAgeError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


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
    
    def __init__(self, nome, cognome, sesso, peso, data_nascita, idbadge, mansione):
        super().__init__(nome, cognome, sesso, peso, data_nascita)
        if data_nascita.year < 18:
            raise IllegalAgeError("Dipendente")

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
        self._idbadge = x
    
    def get_masnione(self):
        return self._mansione
    
    def set_mansione(self, x):
        if(len(x)<0) or (x.isalpha() == False):
            raise('Inserisci una mansione valida')
        else:
            self._mansione = x

    @abstractmethod
    def calcolo_stipendio(self):
        pass


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
            #assert e[1] != 30 and e[3] is True
            if e[1] != 30: 
                assert e[2] is False
        assert isinstance(nome, str)
        assert isinstance(cognome, str)
        assert isinstance(data_di_nascita, datetime)
        for a in alchool:
            assert isinstance(a, tuple)
            assert len(a) == 2
            assert 0 <= a[0] <= 100

        super().__init__(nome, cognome,sesso,peso,data_di_nascita)
        self._matricola = matricola
        self._corso_di_studio = corso_di_studio
        self._alchool = alchool
        self._esami = esami
        logger.info(f"Studente {self._nome} {self._cognome}, matricola {self._matricola}, iscritto al corso di studio "
                    f"{self._corso_di_studio}")

    def __eq__(self, other):
        """
        funziona equal che paragona se due studenti sono uguali usando il numero matricola.
        :param other: oggetto di tipo persona
        :return: True se i due oggetti Studente hanno la stessa matricola altrimenti False.
        """
        return True if self._matricola == other.matricola else False

    def __str__(self):
        return f"Studente {self._nome} {self._cognome}, matricola {self._matricola}, iscritto al corso di studio " \
               f"{self._corso_di_studio}"

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


class LavoratorePiva(Lavoratore):
    def __init__(self,nome, cognome, sesso, peso, data_nascita, idbadge, mansione, tariffa_gg, ore_lavorate):
        super().__init__(nome, cognome, sesso, peso, data_nascita, idbadge, mansione)
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
                 
    def calcolo_stipendio(self):
        stipendio= sum(map(lambda x: x[0] + x[1], self._tariffa_gg.values(),self._ore_lavorate.values())) 
        return stipendio


class Dipendente(Lavoratore):

    @staticmethod
    def check_liv(liv):
        if not isinstance(liv, int) or not 0 < liv <= 7:
            raise LevelError('Inserire un livello corretto')

    def __init__(self, nome, cognome, sesso, peso, data_nascita,  idbadge, mansione, livello):

        super().__init__(nome, cognome, sesso, peso, data_nascita, idbadge, mansione)
        if mansione not in stipendi.keys():
            raise MansioneError("Mansione non presente.")
        Dipendente.check_liv(livello)
        self._livello = livello
        logger.info("E' stato inserito un dipendente.")

    def __str__(self):
        return super().__str__() + ' ' + self._livello

    def __eq__(self, other):
        if isinstance(other, Dipendente):
            if super().__eq__(other) and other._livello == self._livello:
                return True
        return False

    def __hash__(self):
        return hash((super().__hash__(), self._livello))

    def get_livello(self):
        return self._livello

    def set_livello(self, x):
        Dipendente.check_liv(x)
        self._livello = x

    def calcolo_stipendio(self):
        return stipendi.get(self._mansione).get(self._livello)


class FactoryDipendenti:

    @staticmethod
    def createDipendente(tipo, *args, **kwargs):
        if tipo == "Dipendente":
            return Dipendente(*args, **kwargs)
        elif tipo == "LavoratorePiva":
            return LavoratorePiva(*args, **kwargs)


class Check:

    @staticmethod
    def max_tasso_alcolemico(studenti):
        tasso_alcolemico = [s.calcola_tasso_alcolemico() for s in studenti]
        max_tasso = max(tasso_alcolemico)
        return list(filter(lambda x: x.calcola_tasso_alcolemico() == max_tasso, studenti))

        # senza lambda

        # max_tasso = studenti[0].calcolo_tasso_alcolemico()
        # studente_max = studenti[0]
        # for s in studenti[1:]:
        #     if s.calcola_tasso_alcolemico() > max_tasso:
        #         studente_max = s
        # return studente_max

    @staticmethod
    def max_media_studenti(studenti):
        media_studenti = [s.calcolo_media_esami() for s in studenti]
        max_media = max(media_studenti)
        return list(filter(lambda x: x.calcolo_media_esami() == max_media, studenti)) 

    @staticmethod
    def is_ubriaco(studenti):
        ubriaco =  True
        tasso_max = Check.max_tasso_alcolemico(studenti)
        for s in Check.max_media_studenti(studenti):
            if s in tasso_max:
                ubriaco = False
        return ubriaco

    @staticmethod
    def aumento_a_livello(mansione, livello, aumento):
        if mansione not in stipendi.keys():
            raise MansioneError("Mansione non presente.")
        if livello not in stipendi[mansione]:
            raise LevelError("Livello non in mansione")
        if not isinstance(aumento, int):
            raise ValueError("Aumento deve essere di tipo intero")
        stipendi[mansione][livello] = stipendi[mansione][livello] + aumento



class Studenteiva (Studente, LavoratorePiva):
    def __init__(self, nome, cognome, sesso, peso, data_di_nascita, matricola,
                 corso_di_studio, alchool, esami, idbadge, mansione, tariffa_gg, ore_lavorate):
        Studente.__init__(self,nome, cognome, sesso, peso, data_di_nascita, matricola,
                          corso_di_studio, alchool, esami)
        LavoratorePiva.__init__(self,nome, cognome, sesso, peso, data_di_nascita, idbadge, mansione, tariffa_gg, ore_lavorate)
        

        
        