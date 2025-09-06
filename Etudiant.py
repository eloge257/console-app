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
            etudiants = []
            for i in range(nombre):
                print("Etudiant numero:", i+1)
                nom = input("Nom de l'etudiant:")
                prenom = input("Prenom de l'etudiant:")
                age = int(input("Age de l'etudiant:"))
                formation = input("Formation de l'etudiant:")
                etudiant = Etudiant(nom, prenom, age, formation)
                etudiants.append(etudiant.to_dict())
            # Sauvegarde tous les étudiants dans le fichier JSON
            Etudiant.sauvegarder_etudiant_json(etudiants, "etudiants.json")
            print("Etudiants sauvegardés dans etudiants.json")
         
        def to_dict(self):
            return {
                "nom": self.nom,
                "prenom": self.prenom,
                "age": self.age,
                "formation": self.formation
            }


        @staticmethod
        def sauvegarder_etudiant_json(etudiants, filename):
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(etudiants, f, ensure_ascii=False, indent=4)

# etudiant = Etudiant("Dupont", "Jean", 22, "Informatique")
# sauvegarder_etudiant_json(etudiant, "etudiant.json")