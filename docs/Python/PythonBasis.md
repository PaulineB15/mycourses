# Mes premiers pas avec Python

## 1. Affichage et Commentaires (`print` et `#`)

En Python, la fonction `print()` permet d'afficher du texte ou des résultats à l'écran. C'est l'outil de base pour communiquer avec l'utilisateur.
Les commentaires commencent par un `#`. Ils sont ignorés par l'ordinateur et servent à documenter le code pour les humains.

```python
# Ceci est un commentaire, il ne s'affichera pas
print("Bonjour le monde !") 
print(42) # On peut aussi afficher des nombres
````

## 2. Variables et types de données

Une variable est comme une boîte dans laquelle on stocke une information. En Python, il n'y a pas besoin de déclarer le type de la variable à l'avance, le langage le devine automatiquement.

Les 4 types principaux à connaître :

- str (String) : Chaîne de caractères (texte).

- int (Integer) : Nombre entier.

- float : Nombre à virgule (on utilise un point en Python).

- bool (Boolean) : Vrai ou Faux (True ou False).

```python
- prenom = "Pauline"      # type: str
- age = 25                # type: int
- taille = 1.65           # type: float
- est_developpeuse = True # type: bool

# On peut afficher plusieurs variables en les séparant par des virgules
print("Je m'appelle", prenom, "et j'ai", age, "ans.")
```

## 3. Les Conditions (if / else)
Les conditions permettent au programme de prendre des décisions. L'indentation (les espaces au début de la ligne) est obligatoire en Python pour indiquer ce qui se trouve à l'intérieur de la condition.

```python
age_utilisateur = 20

if age_utilisateur >= 18:
    print("Vous êtes majeur(e).")
else:
    print("Vous êtes mineur(e).")

# On peut aussi utiliser elif (sinon si) pour plus de conditions
note = 15
if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Assez bien")
else:
    print("Il faut réviser")
```

## 4. Les Boucles (`for` et `while`)

Les boucles permettent de répéter une action plusieurs fois sans avoir à copier-coller du code.

**La boucle `for`** est idéale quand on sait à l'avance combien de fois on veut répéter l'action, ou pour parcourir une collection (comme une liste).
```python
# Répéter une action 3 fois (0, 1, 2)
for i in range(3):
    print("Tour de boucle numéro", i)
```
La boucle while (tant que) continue de s'exécuter tant qu'une condition précise reste vraie. Attention aux boucles infinies si la condition ne devient jamais fausse !    

```python
compteur = 0
while compteur < 3:
    print("Le compteur est à", compteur)
    compteur = compteur + 1 # Crucial pour que la boucle s'arrête un jour
```

## 5. Les Structures de données (list, dict, tuple, set)
Parfois, une simple variable ne suffit pas. On utilise alors des structures de données pour regrouper plusieurs valeurs.

Les Listes (list) : Une collection ordonnée et modifiable. On y accède par la position de l'élément (attention, l'index commence toujours à 0).
```python
langages = ["Python", "HTML", "CSS"]
print(langages[0]) # Affiche "Python"

langages.append("JavaScript") # Ajoute un élément à la fin de la liste
print(langages)
```
Les Dictionnaires (dict) : Ils fonctionnent avec un système de "clé: valeur", un peu comme une fiche de renseignement ou un répertoire.

```python
utilisateur = {
    "nom": "Pauline",
    "age": 25,
    "role": "Développeuse Web"
}
print(utilisateur["nom"]) # Affiche "Pauline"
```
Notes rapides sur les autres structures :

- Tuple : Comme une liste, mais on ne peut plus la modifier une fois créée (ex: coordonnees = (10, 20)).

- Set : Un ensemble d'éléments uniques, sans ordre défini (ex: couleurs = {"rouge", "bleu"}).


## 6. Interaction avec l'utilisateur (input)
Pour rendre un script interactif, on demande des informations à l'utilisateur avec input().

Attention : input() renvoie toujours du texte (str). Si tu attends un nombre (pour calculer un âge par exemple ou vérifier une condition mathématique), il faut le convertir explicitement avec int().
```python
# Demander du texte
prenom = input("Quel est ton prénom ? ")
print("Enchantée", prenom)

# Demander un nombre et le convertir
age_str = input("Quel est ton âge ? ")
age = int(age_str) # On transforme le texte en nombre entier

if age >= 18:
    print("Tu es majeure.")
else:
    print("Tu es mineure.")
```