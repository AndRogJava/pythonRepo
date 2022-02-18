from persona import Lavoratore


class LavoratorePiva(Lavoratore):
    super().__init__(nome, cognome, data_nascita, sesso, peso, idbaige, mansione)
    
    
    def stipendio(self):
        return tariffa_giornaliera + ore_lavorate 
        