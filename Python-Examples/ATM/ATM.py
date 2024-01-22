class Bankomat:
    def __init__(self):
        self.saldo = 0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.saldo += betrag
            return f'{betrag} EUR wurden eingezahlt. Neuer Kontostand: {self.saldo} EUR'
        else:
            return 'Ungültiger Betrag für Einzahlung.'


    def abheben(self, betrag):
        if betrag > 0 and betrag <= self.saldo:
            self.saldo -= betrag
            return f'{betrag} EUR wurden abgehoben. Neuer Kontostand: {self.saldo} EUR'
        elif betrag > self.saldo:
            return 'Nicht genügend Guthaben auf dem Konto.'
        else:
            return 'Ungültiger Betrag für Abhebung.'

    def kontostand(self):
        return f'Ihr aktueller Kontostand beträgt: {self.saldo} EUR'

# Hauptprogramm
bankomat = Bankomat()

while True:
    print("\nBankomaten-Simulator")
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand")
    print("4. Beenden")

    auswahl = input("Bitte wählen Sie eine Option (1/2/3/4): ")

    if auswahl == '1':
        betrag = float(input("Geben Sie den Einzahlungsbetrag ein: "))
        print(bankomat.einzahlen(betrag))
    elif auswahl == '2':
        betrag = float(input("Geben Sie den Abhebungsbetrag ein: "))
        print(bankomat.abheben(betrag))
    elif auswahl == '3':
        print(bankomat.kontostand())
    elif auswahl == '4':
        print("Vielen Dank, dass Sie den Bankomaten-Simulator genutzt haben. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine der verfügbaren Optionen (1/2/3/4).")
