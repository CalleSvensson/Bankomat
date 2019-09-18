konto = {}

def KollaNummer(text):
    while True:
        try:
            val = int(input(text))
            return val
        except:
            print("Ej tillgängligt, använd siffror. ")

def Meny1():
    nummer = KollaNummer("Ange kontonummer: ")
    if nummer in konto:
        print("Konto finns redan. ")
    else:
        konto[nummer]= 0
        print(f"Konto {nummer} skapat. ")


def Meny2():
    nummer = int(input("Ange kontonummer: "))
    if nummer not in konto:
        print("Konto finns ej. ")
        return
    print(f"Välkommen {nummer}")
    saldo = konto[nummer]
    while True:
        print(f"*** Inloggad som {nummer} ***")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Logga ut")
        val = KollaNummer("Välj: ")
        if val == 1:
            uttag = KollaNummer("Ange belopp: ")
            if saldo >= uttag and uttag > 0:
                print(f"{uttag} uttaget. ")
                saldo = saldo - uttag
                konto[nummer] = saldo
            else:
                print("Ej tillgängligt.")
        elif val == 2:
            insatt = KollaNummer("Ange belopp: ")
            if insatt > 0:
                print(f"{insatt} insatt på ditt konto. ")
                saldo = saldo + insatt
                konto[nummer] = saldo
            else:
                print("Ej tillgängligt. ")
        elif val == 3:
            print(f"Ditt saldo är: {saldo}. ")   
        elif val == 4:
            break
        else:
            print("Val finns ej. ")


while True:
    print("*** HUVUDMENY ***")
    print("1. Skapa konto")
    print("2. Logga in konto")
    print("3. Avsluta")
    val = KollaNummer("Välj: ")
    if val == 1:
        Meny1()
    elif val == 2:
        Meny2()
    elif val == 3:
        break
    else:
        print("Val finns inte. ")