from persona import Lavoratore


class LavoratorePiva(Lavoratore):
    def __init__(self,nome, cognome, data_nascita, sesso, peso, idbadge, mansione,tariffa_gg, ore_lavorate):
        super().__init__(nome, cognome, data_nascita, sesso, peso, idbadge, mansione, tariffa_gg, ore_lavorate)
        self._tariffa_gg=tariffa_gg
        self._ore_lavorate=ore_lavorate
        
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
        