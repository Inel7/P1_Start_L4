# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

def vind_grootste_getal():
    lijst = [1, 2, 3, 4, 5]
    grootste_getal = lijst[0]
    for i in lijst :
        if i > grootste_getal:
            grootste_getal=i
    print(grootste_getal)
vind_grootste_getal()

