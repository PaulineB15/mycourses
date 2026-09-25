# PRÉPARATION 
# LISTES - Création du "classeur" vide. Il faut qu'il existe 
# avant qu'on puisse y ranger quoi que ce soit.
utilisateurs = []

# ENTRÉE DES DONNÉES (Interactions)
# Le programme s'arrête et attend que le prénom soit tapé.
prenom = input("Quel est ton prénom ? ")
print("Enchantée", prenom)

# Le programme attend l'âge. Le '+' pour intégrer le prénom dans la question.
age = input("Quel est ton age " + prenom + "?")
# L'âge tapé est du texte (ex: "25"). int -> vrai nombre mathématique (25)
age_chiffre = int(age)
print("Merci", prenom)

# TRAITEMENT
# DICTIONNAIRE - Création une "fiche" (le dictionnaire) qui regroupe les infos de l'utilisateur.
profil = {"nom": prenom, "age": age_chiffre}

# Conditions
if age_chiffre >=18:
    print("Vous êtes majeur(e).")
else:      
    print("Vous êtes mineur(e).")

# STOCKAGE
# Ranger la "fiche" (profil) dans le "classeur" (utilisateurs).
utilisateurs.append(profil)

# SORTIE (Affichage final) 
# La boucle va parcourir chaque élément de la liste
# La variable 'personne' représente la fiche que l'ordinateur est en train de lire.
for personne in utilisateurs: 
    # À chaque tour de boucle, la variable "personne" contient un dictionnaire de la liste.
    # On peut donc accéder à ses clés "nom" et "age" :
    nom_personne = personne["nom"]
    age_personne = personne["age"]

    # Affiche les données à l'écran.
    print("Le prénom est", nom_personne, "et l'âge est", age_personne)

    # Commande pour afficher dans le terminal
    # python docs/Python/MiniProjet.py