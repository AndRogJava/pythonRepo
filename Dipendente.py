from ast import match_case


class Dipendente(Lavoratore):
    def __init__(self,nome, cognome, data_nascita, sesso, peso, idbadge, mansione, livello):
        super().__init__(nome, cognome, data_nascita, sesso, peso, idbadge, mansione)
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

    def set_idbadge(self, x):
        Lavoratore.check_id(x)
        self._livello = x
    
    @staticmethod
    def check_liv(liv):
        if isinstance(liv,int) and liv>0:
            pass
        else:
            raise('Inserire un livello corretto')
    
    def calcolo_stipendio(self, mansione, livl):
        item = [mansione, livl]
        match item:
            case [7, 'addetto pulizie']:
                stipendio = 1275.00
            case [7, 'inserviente']:
                stipendio = 1230.00
            case [6, 'operaio comune']:
                stipendio = 1392.00
            case [6, 'fattorino']:
                stipendio = 1359.00
            case [5, 'impiegato']:
                stipendio = 1476.00
            case [5, 'operaio qualificato']:
                stipendio = 1494.00
            case [4, "impiegato d'ordine"]:
                stipendio = 1600.00
            case [4, 'operaio specialzzato']:
                stipendio = 1610.00
            case [3, 'impiegato di concetto']:
                stipendio = 1772.00
            case [3, 'operaio specializzato provetto']:
                stipendio = 1789.00
            case [2, 'impiegato autonomo']:
                stipendio = 1988.00
            case [2, 'impiegato direttivo']:
                stipendio = 1979.00
            case [1, 'manager']:
                stipendio = 2670.00
            case [1, 'direttore']:
                stipendio = 2790.00
            case [1, 'responsabile']:
                stipendio = 2390.00
            case _:
                return ("Errore nel calcolo dello stipendio")
        return stipendio