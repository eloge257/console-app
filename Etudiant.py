from Personne import Personne
import json

class Etudiant(Personne):
        def __init__(self,nom,prenom,age,formation):
            Personne.__init__(self,nom,prenom,age)
            self.formation = formation
        def afficher(self):
         print(self.nom,self.prenom,self.age,self.formation)
    
        def create_etudiant(self):        
         nombre = int(input("Combien d'etudiants voulez-vous creer?"))
         dict=[]
         for i in range (nombre):
            print("Etudiant numero:",i+1)
            self.nom = input("Nom de l'etudiant:")
            self.prenom = input("Prenom de l'etudiant:")
            self.age = int(input("Age de l'etudiant:"))
            self.formation = input("Formation de l'etudiant:")
            dict.append(self.__dict__)
        
         print(dict)
        def to_dict(self):
            return {
                "nom": self.nom,
                "prenom": self.prenom,
                "age": self.age,
                "formation": self.formation
            }


def sauvegarder_etudiant_json(etudiant, filename):
    with open(filename, "w", encoding="utf-8") as f:
     json.dump(etudiant.to_dict(), f, ensure_ascii=False, indent=4)

etudiant = Etudiant("Dupont", "Jean", 22, "Informatique")
sauvegarder_etudiant_json(etudiant, "etudiant.json")