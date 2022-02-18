from pickle import FALSE
from persona import Dipendente, LavoratorePiva, Studente, Check, stipendi, Studenteiva, StudenteDip
from datetime import datetime



if __name__ == "__main__":

    studenti_list = [ Studente('Fabiana', 'Verdi', False, 51, datetime(1995,3,10), 1, 'Filosofia', [(70, 200), (30, 50)], {'Metafisica':(10, 30, True)}),
                      Studente('Nicola', 'Rossi', True, 79, datetime(1994,3,10), 2, 'Biologia', [(17, 300), (45, 100)], {'Biochimica':(8, 28, False)}),
                      Studente('Giovanni', 'Venti', True, 83, datetime(1994,5,12), 3, 'Filosofia', [(20, 50), (30, 100)], {'Etica':(10, 18, False)}),
                      Studente('Bianca', 'Sandri', False, 47, datetime(1997,7,9), 4, 'Psicologia', [(15, 200), (20, 200)], {'Statistica':(10, 20, False)}),
                      Studente('Walid', 'Abdellatif', True, 78, datetime(1994,4,16), 4, 'Ingegneria', [], {'Analisi II':(12, 30, True)})
                       ]

    dipendenti_list = [ Dipendente('Fabiana', 'Verdi', False, 51, datetime(1995,3,10), 1, 'addetto_pulizia', 2),
                      Dipendente('Nicola', 'Rossi', True, 79, datetime(1994,3,10), 2, 'inserviente', 3),
                      Dipendente('Giovanni', 'Venti', True, 83, datetime(1994,5,12), 3, 'operaio', 7),
                      Dipendente('Bianca', 'Sandri', False, 47, datetime(1997,7,9), 4, 'fattorino', 5),
                      Dipendente('Walid', 'Abdellatif', True, 78, datetime(1994,4,16), 4, 'Driettore', 7)
                       ]
    lavoratoriPIva_list = [ LavoratorePiva('Fabiana', 'Verdi', False, 51, datetime(1995,3,10), 1, 'consulente', 300, 5),
                      LavoratorePiva('Nicola', 'Rossi', True, 79, datetime(1994,3,10), 2, 'venditore', 450, 6),
                      LavoratorePiva('Giovanni', 'Venti', True, 83, datetime(1994,5,12), 3, 'istruttore', 100, 7),
                      LavoratorePiva('Bianca', 'Sandri', False, 47, datetime(1997,7,9), 4, 'fattorino', 300, 5),
                      LavoratorePiva('Walid', 'Abdellatif', True, 78, datetime(1994,4,16), 4, 'Driettore', 500, 6)
                       ]
    for i in studenti_list:
        print(i)

    for i in Check.max_media_studenti(studenti_list):
        print(i)

    for i in Check.max_tasso_alcolemico(studenti_list):
        print(i)

    print(Check.is_ubriaco(studenti_list))
    
    Check.aumento_a_livello('inserviente', 5, 2000)
    print(stipendi)
    
    mix_list = list()
    mix_list.extend(studenti_list)
    mix_list.extend(dipendenti_list)
    mix_list.extend(lavoratoriPIva_list)
    mix_list.append(Studenteiva('Fabiana', 'Verdi', False, 51, datetime(1995,3,10), 1, 'Filosofia', [(70, 200), (30, 50)], {'Metafisica':(10, 30, True)},1, 'consulente', 300, 5))

    mix_list.append(StudenteDip('Fabiana', 'Bianchi', False, 51, datetime(1995, 3, 10), 1, 'Filosofia', [(70, 200), (30, 50)],
                      {'Metafisica': (10, 30, True)}, 1, 'consulente', 4))
    solo_stud_lavoratori = list(filter(lambda x: isinstance(x, Studenteiva) or isinstance(x, StudenteDip), mix_list))
    for i in solo_stud_lavoratori:
        print(i)
