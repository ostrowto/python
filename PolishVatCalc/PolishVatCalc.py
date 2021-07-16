import os

cena = float(input("Podaj cenę: "))

def policz_brutto(netto, stawka_vat_23):
    return netto + netto * stawka_vat_23


stawka_vat_23 = 0.23
brutto_23 = policz_brutto(cena, stawka_vat_23)
print(f'Produkt o cenie {cena} PLN netto i stawce Vat {round(stawka_vat_23*100)}% kosztuje {round(brutto_23, 2)} PLN')


def policz_brutto(netto, stawka_vat_8):
    return netto + netto * stawka_vat_8


stawka_vat_8 = 0.08
brutto_8 = policz_brutto(cena, stawka_vat_8)
print(f'Produkt o cenie {cena} PLN netto i stawce Vat {round(stawka_vat_8*100)}% kosztuje  {round(brutto_8, 2)} PLN')



def policz_brutto(netto, stawka_vat_5):
    return netto + netto * stawka_vat_5


stawka_vat_5 = 0.05
brutto_5 = policz_brutto(cena, stawka_vat_5)
print(f'Produkt o cenie {cena} PLN netto i stawce Vat {round(stawka_vat_5*100)}% kosztuje  {round(brutto_5, 2)} PLN')

print(f'\nUwaga wyniki zaokrąglono do dwóch miejsc po przecinku')

os.system("pause")
