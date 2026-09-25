# Création de la classe
class Utilisateur:
    def __init__(self, nom_utilisateur, age_utilisateur):
        self.nom = nom_utilisateur
        self.age = age_utilisateur

    def dire_bonjour(self):
        # Le "f" => f-string en Python. C'est pour indiquer qu'il y a des variables
        # à l'intérieur des accolades et qu'il faut les remplacer par leur valeurs
        print(f"Bonjour, je suis {self.nom} et j'ai {self.age} ans.")


# Copie du 1er projet " MiniProjet.py"
utilisateurs = []

prenom = input("Quel est ton prénom ? ")
age_texte = input(f"Quel est ton âge {prenom} ? ")
age_chiffre = int(age_texte)

if age_chiffre >= 18:
    print("Vous êtes majeur(e).")
else:
    print("Vous êtes mineur(e).")

# C'est ici que la méthode POO opère : 
# On remplace le dictionnaire par la création d'un Objet Utilisateur
profil = Utilisateur(prenom, age_chiffre)

utilisateurs.append(profil)

# Boucle finale simplifiée grâce à l'Objet
print("\n--- Liste des utilisateurs enregistrés ---")
for personne in utilisateurs:
    # L'objet "personne" sait comment s'afficher tout seul grâce à sa méthode !
    personne.dire_bonjour()