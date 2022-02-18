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




