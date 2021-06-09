from datetime import date

today = date.today()
print("\nJour Actuel:", today)
try:
    year = int(input("Année: "))
except ValueError:
    raise ValueError("Année invalide ! Vous devez entrer un numéro pour l'année.")
try:
    month = int(input("Mois: "))
except ValueError:
    raise ValueError("Mois invalide ! Vous devez entrer un numéro pour le mois.")
try:
    day = int(input("Jour: "))
except ValueError:
    raise ValueError("Jour invalide ! Vous devez entrer un numéro pour la journée.")

try:
    futureday = date(year, month, day)
except ValueError:
    raise ValueError("Date invalide! Vous devez saisir une date valide.")

if today > futureday:
    raise ValueError("Date invalide! Vous devez choisir une date future.")

delta = futureday - today
print("\nIl y a", delta.days, "jours entre", today, "et", futureday, "!")