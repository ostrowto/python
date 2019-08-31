from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

kolory = ('czerwony', 'pomaranczowy', 'zolty', 'zielony', 'blekitny', 'niebieski', 'fioletowy')
wartosci = (1, 2, 3, 4, 5, 6, 7)
liczba_kart = 7


def inicjalizacja():
    global gracze, talia, tlo, rece, palety, tura_gracza
    talia = []
    for kolor in kolory:
        for wartosc in wartosci:
            talia.append((wartosc, kolor))
    random.shuffle(talia)

    gracze = [
                {'nazwa': 'Pierwszy', 'numer': 1, 'aktywnosc': True},
                {'nazwa': 'Drugi', 'numer': 2, 'aktywnosc': True},
                {'nazwa': 'Trzeci', 'numer': 3, 'aktywnosc': True},
            ]
    tlo = []
    rece = {1: [], 2: [], 3: []}
    palety = {1: [], 2: [], 3: []}

    tlo.append( (0, 'czerwony') )


def rozdaj_karty():
    global talia, liczba_kart
    for i in range(liczba_kart):
        for g in gracze:
            rece[  g['numer']  ].append( talia.pop() )


def nastepny_gracz():
    global tura_gracza
    if 1 >= aktywni_gracze():
        return False
    znaleziony = False
    while not znaleziony:
        tura_gracza += 1
        if tura_gracza > len(gracze):
            tura_gracza %= len(gracze)
        if gracze[tura_gracza-1]['aktywnosc']:
            znaleziony = True
    return True

def aktywni_gracze():
    global gracze

    i = 0
    for gracz in gracze:
       if gracz['aktywnosc']:
        i += 1
    return i

def wybierz_rozpoczynajacego():
    global tura_gracza
    tura_gracza = 1


@app.route('/nastepny')
def nastepny():
    global tlo
    #sprawdzenie stanu na koniec tury gracza

    if tlo[-1][1] == 'czerwony':
        najwyzsze = {}
        for gracz in gracze:
            for karta in palety[gracz['numer']]:
                if gracz['numer'] in najwyzsze:
                    if karta[0] > najwyzsze[gracz['numer']][0]:
                        najwyzsze[gracz['numer']] = karta
                    elif karta[0] == najwyzsze[gracz['numer']][0]:
                        if kolory.index(karta[1]) < kolory.index(najwyzsze[gracz['numer']][1]):
                            najwyzsze[gracz['numer']] = karta
                else:
                    najwyzsze[gracz['numer']] = karta
        wygrywajacy_gracz = None
        wygrywajaca_karta = ('', '')
        for gracz in gracze:
            if gracz['numer'] in najwyzsze and najwyzsze[gracz['numer']][0] >= wygrywajaca_karta[0]:
                wygrywajaca_karta = najwyzsze[gracz['numer']]
                wygrywajacy_gracz = gracz['numer']
            elif gracz['numer'] in najwyzsze and najwyzsze[gracz['numer']][0] == wygrywajaca_karta[0]:
                if kolory.index(najwyzsze[gracz['numer']][1]) < kolory.index(wygrywajaca_karta[1]):
                    wygrywajaca_karta = najwyzsze[gracz['numer']]
                    wygrywajacy_gracz = gracz['numer']
        if wygrywajacy_gracz != tura_gracza:
            gracze[tura_gracza-1]['aktywnosc'] = False


    elif tlo[-1][1] == 'pomaranczowy':
        pass
    elif tlo[-1][1] == 'zolty':
        pass
    elif tlo[-1][1] == 'zielony':
        pass
    elif tlo[-1][1] == 'blekitny':
        pass
    elif tlo[-1][1] == 'niebieski':
        pass
    elif tlo[-1][1] == 'fioletowy':
        pass

    #przejście do następnego

    if 1 >= aktywni_gracze():
        return redirect('/koniec')
    elif nastepny_gracz():
        return '<a href="wybierz_na_tlo">następny gracz '+str(tura_gracza)+'</a>'
        # tutaj dodać templatkę
    else:
        return redirect('/koniec')


@app.route('/koniec')
def koniec():
    return "Wygrał gracz nr "+str(gracze[tura_gracza]['numer'])+" - "+gracze[tura_gracza]['nazwa']
    #tutaj dodać templatkę

@app.route('/')
def start():
    inicjalizacja()
    rozdaj_karty()
    wybierz_rozpoczynajacego()
    return redirect('/wybierz_na_tlo')


@app.route('/wybierz_na_tlo')
def wybierz_na_tlo():
    global juz_rzucona

    juz_rzucona = False
    if( not len(rece[tura_gracza]) ):
        gracze[tura_gracza-1]['aktywnosc'] = False
        return redirect('/nastepny')

    return render_template('plansza.html', tlo=tlo, rece=rece, gracze=gracze, palety=palety, tura_gracza=tura_gracza, gdzie='tlo')

@app.route('/wybierz_na_palete')
def wybierz_na_palete():
    global gracze, juz_rzucona

    if( not len(rece[tura_gracza]) ):
        if not juz_rzucona: #przegrywa jeśli nie rzucił na tło
            gracze[tura_gracza-1]['aktywnosc'] = False
        return redirect('/nastepny')
    czy_moze_pominac = juz_rzucona

    return render_template('plansza.html', tlo=tlo, rece=rece, gracze=gracze, palety=palety, tura_gracza=tura_gracza, gdzie='paleta', czy_moze_pominac=czy_moze_pominac)


@app.route('/rzuc_na_tlo/<karta>')
def rzuc_na_tlo(karta):
    global tura_gracza, juz_rzucona

    rzucona_podzielona = karta.split('_')

    if [(wartosc, kolor) for (wartosc, kolor) in rece[tura_gracza] if wartosc==int(rzucona_podzielona[0]) and kolor==rzucona_podzielona[1]]: #byla w rece
        juz_rzucona = True
        rzucona = (rzucona_podzielona[0], rzucona_podzielona[1])
        tlo.append(rzucona)
        rece[tura_gracza] = [(wartosc, kolor) for (wartosc, kolor) in rece[tura_gracza] if wartosc!=int(rzucona_podzielona[0]) or kolor!=rzucona_podzielona[1]]
        return redirect('/wybierz_na_palete')

    return redirect('/wybierz_na_tlo')


@app.route('/rzuc_na_palete/<karta>')
def rzuc_na_palete(karta):
    global tura_gracza

    rzucona_podzielona = karta.split('_')

    if [(wartosc, kolor) for (wartosc, kolor) in rece[tura_gracza] if wartosc==int(rzucona_podzielona[0]) and kolor==rzucona_podzielona[1]]: #byla w rece
        rzucona = (rzucona_podzielona[0], rzucona_podzielona[1])
        palety[tura_gracza].append(rzucona)
        rece[tura_gracza] = [(wartosc, kolor) for (wartosc, kolor) in rece[tura_gracza] if wartosc!=int(rzucona_podzielona[0]) or kolor!=rzucona_podzielona[1]]
        return redirect('/nastepny')

    return redirect('/wybierz_na_palete')














if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
