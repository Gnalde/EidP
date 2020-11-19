def ende():
    print()
    print("Du hast gewonnen!")

def a_attacke1():
    print()
    print("Du wirfst deine Turing-Maschine auf CrazyFrog!")
    ende()

def a_attacke2():
    print()

def a_attacke3():
    print("Hello")

def c_attacke1():
    print()

def c_attacke2():
    print()

def c_attacke3():
    print()

def intro():
    print()
    print("Wähle eine Attacke. [ 1 / 2 / 3 ]")

    attacke = str(input("Du wählst: "))

    if (attacke == "1"):
        a_attacke1()
    elif (attacke == "2"):
        a_attacke2()
    else:
        a_attacke3()

def auswahl():

    charakterwahl = str(input("Du wählst: "))

    if (charakterwahl == "CrazyFrog"):
        print()
        print("Du hast dich für CrazyFrog entschieden, dein Gegner ist Alan Turing!")
        intro()
    elif (charakterwahl == "Alan Turing"):
        print()
        print("Du hast dich für Alan Turing entschieden, dein Gegner ist CrazyFrog!")
        intro()
    else:
        print()
        print("Du musst dir schon einen Charakter aus der Geschichte aussuchen, sonst funktioniert das hier nicht ;)")
        print("Versuchs nochmal! [ CrazyFrog / Alan Turing ]")
        auswahl()

print("##############################")
print("# Willkommen bei Clash&Bash! #")
print("##############################\n")
print("Entscheide dich zuerst für deinen Charakter. [ CrazyFrog / Alan Turing ]")
auswahl()