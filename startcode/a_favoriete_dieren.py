# Maak een programma dat:
# - een lege lijst aanmaakt
# - drie dieren vraagt aan de user
# - deze dieren toevoegt aan de lijst
# - de lijst met dieren toont aan de user
lijst = []
for i in range(1,4):
    dier = input("Geef je favoriet dier ")
    lijst.append(dier)
print("dit zijn je favoriete dieren", lijst)