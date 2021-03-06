
class Soucet:

    # Zdroj významov čísel: https://www.numerologia.sk/clanky/vyznam-cisel-19.html
    vyznamy_cisel = {                        # vytvoril som slovnik v ktorom su na lavej strane kluce, na pravej hodnoty
      "1": "začiatok, počatie, vývoj",      # v slovniku su zadefinovane vyznamy jednotlivych jednocifernych cisel
      "2": "rozmnoženie, pohyb nahor",
      "3": "viera, nádej a láska",
      "4": "nehoda, rozklad, smrť",
      "5": "symbol tvorivosti",
      "6": "splnené túžby, vyrovnanosť, spokojnosť, harmónia",
      "7": "svetlo, pokoj, šťastie, oddych po práci",
      "8": "dvojitý zápor, ktorý sa ruší a vytvára klad",
      "9": "tvorenie, splnenie plánov, dosiahnutie úspechov"
    }

    def rozdelenie_cisla(self, cislo):

        zoznam_cislo = list(cislo)  # rozdelenie zadaneho cisla na zoznam

        sucet = 0  # vytvaram premmenu do ktorej sa uklada sucet, zaciname s 0
        scitavane_cislice = []
        for i in range(len(zoznam_cislo)):  # zistime pocet cisel ktore sa nachadzaju v zozname
            sucet += int(zoznam_cislo[i])  # scitavame jednotlive cisla v zozname napr. 0+5 potom 5+8, 8+9, 9+5
        if len(str(sucet)) > 1:  # pokial je vysledok suctu viac ako jednociferne cislo tak musime opakovat predosly krok
            zoznam_sucet = list(str(sucet))  # rozdelenie vysledku na zoznam
            # print(f'zoznam_sucet: {zoznam_sucet}')
            sucet = 0
            for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
                sucet += int(zoznam_sucet[i])  # scita jednotlive cleny zoznamu
            if len(str(sucet)) > 1:  # znova, pokial je vysledok viac ako jednociferne cislo
                zoznam_sucet = list(str(sucet))  # rozdeli cislo na zoznam
                sucet = 0
                for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
                    sucet += int(zoznam_sucet[i])   # postupne scita jednotlive cleny zoznamu

#        print(f'Výsledok súčtu číslic v čísle: {cislo} je: {sucet}')
        return sucet  # príkaz return nám vráti výsledok s ktorým budeme pracovat dalej

    def vyznam_cisla(self, cislo):
        vyznam = self.vyznamy_cisel.get(str(cislo))  # zo zadefinovaného slovníku získame číslo, ktoré vyšlo predtým ako výsledok rozdelenia
        return vyznam
#        print(f'Význam čísla: {cislo} v numerológií je: {vyznam}')

