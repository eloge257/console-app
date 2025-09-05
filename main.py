from Etudiant import Etudiant
from Personne import Personne
 
#  ```Programme principal```

menu = """
1.creer un etudiant
2.afficher les etudiants
3.quitter
"""
print(menu)
menu_choix = int(input("Choisisser une option:"))
while menu_choix != 3:
    if menu_choix == 1:
        e1 = Etudiant(nom="", prenom="", age=0,formation="")
        e1.create_etudiant()
    elif menu_choix == 2:
        e1.afficher()
    else:
        print("Choix invalide")
    print(menu)
    menu_choix = int(input("Choisisser une option:"))
print("---------------------------------------------")

