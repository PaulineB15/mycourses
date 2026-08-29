# JavaScript Basis

JavaScript (JS) : est un langage de programmation côté client. Il permet de rendre les
pages web interactives et dynamiques (modifier le contenu, réagir aux clics, animer des
éléments) sans avoir besoin de recharger la page.

Où écrire du JavaScript ?

Le JavaScript s'exécute directement dans le navigateur. Il s'intègre généralement dans une page HTML avec des balises `<script>`. 

![Js Script](../Images/JavascriptScript.png)

## 1. Débuter avec Js

### a. Basic syntax
- JavaScript is case-sensitive. Lines end by `;`
 - Block are delimited curly brackets by `{ }`
 - Comments are between `/* */` for multiple lines or after `//` for one line.

 ### b. Affichage 

- `console.log("Coucou");`

Affiche des informations dans la console du navigateur ou de l'environnement d'exécution (comme Node.js).

C'est l'outil essentiel du développeur pour le débogage. Il permet de vérifier la valeur d'une variable ou le flux d'exécution du programme sans affecter l'interface utilisateur.

- `alert("Hello World !");`

Affiche une pop-up directement à l'utilisateur.

Principalement utilisé pour les messages d'avertissement ou de confirmation simples, mais il est souvent évité dans les applications modernes pour une meilleure expérience utilisateur.

## 2. Variables & Types de données

### Declare a variable with:
- `Const` - Valeur qui ne change pas
- `Let` - Valeur qui change
- *`Var`- Ancienne manière de déclarer. A éviter*

*Example :*

```js
const firstName = "Pauline"; // Ne peut pas être modifier
let age = 38;                
let etudiante = true;        // Peut être modifié  
```

<!-- termynal -->

```
$ node
> const nomProduit = "Clavier"
undefined
> let prixHT = 45
undefined
> prixHT = 39
39
> nomProduit = "Souris"
Uncaught TypeError: Assignment to constant variable.
# const refuse d'être réaffecté, let l'accepte
```
---

### a. Types
- `String`- Text that is wrap it in `''`or `""`
- `Number`- 2 types of numbers: `integer (30)` and `floating (5.2)`
- `Boolean`- To test a condition `(true of false)`
- `Undefined` -	Variable déclarée mais non définie	let x;
- `Null` -	Valeur intentionnellement vide	let y = null;

<!-- termynal -->

```
> typeof "Clavier"
'string'
> typeof 45
'number'
> typeof true
'boolean'
# Le piège du + avec une chaîne
> 45 + 3
48
> "Prix : " + 45
'Prix : 45'
```

---


*Example :*

```js
let welcomeMessage = "Hello Pauline !"; 
// String (Chaîne de caractère) 
let age = 38;                          // Number 
let etudiante = true;                 // Boolean (true/false)
```

### b. String concatenation
Assembler des morceaux de texte et variables.

#### Simple concatenation

*Example :*

```js
const prenom = "Pauline";
const nom = "Bennoin";

// On additionne les variables et un espace au milieu
const nomComplet = prenom + " " + nom; 

console.log(nomComplet); // Résultat : "Pauline Bennoin"
```

#### Backsticks concatenation
Utilise les `backsticks (``) et variables ($)` pour insérer directement les variables. C'est la méthode moderne et recommandé car plus lisible.

```js
const prenom = "Pauline";
const nom = "Bennoin";

const nomComplet = `${prenom} ${nom}`;

console.log(nomComplet); // Affiche : "Pauline Bennoin"
```

⚠️**CAUTION** <br>
Pour inclure une apostrophe ( ' ) dans une chaine délimité par des guillets simple ( ' ), il faut l'échapper avec un anti-slash ( \ ).

```js
const phrase = 'C\'est le dossier de pauline bennoin';
console.log(phrase); // Affiche : C'est le dossier de pauline bennoin
```

### c. Other types
- `Array` - Liste ordonnée de valeurs. Commence à partir de **l'index 0**.


*Example :*

```js
let user = ["Je","Pauline", 38, true]; 

console.log(user[1]);    // Affiche l'élément à l'index 1 (soit Pauline)

```
```text
> let user = ["Je", "Pauline", 38, true]; 
> console.log(user[1]);
Pauline
```

- `Object` - Ensemble de données non ordonné sous forme de propriétés (clé: valeur)

*Example :*

```js
let user = {
    name:"Pauline",     // clé: name et valeur: "Pauline"
    age: 38,
    school:"La Fabrique du Numérique}; 

console.log(user.age);  // Accès à la valeur par le nom de la clé
```
```js
// Ajouter une propriété à un objet:
user.nickname = "Paupau"
```



## 3. Operators 

### a. Opérateurs Arithmétiques
Arithmetic operators are used for performing mathematical calculations in JavaScript.

![Arithmetic operators](../Images/ArithmeticOperators.png)

### b. Opérateurs d'affectation (raccourcis)
Permet de modifier la valeur d'une variable en utilisant sa valeur actuelle

![Assignement operators](../Images/Operators.png)

### c. Opérateurs d'égalité
- `Egalité simple (==)` : Convertit automatiquement les types si nécessaire, puis compare uniquement les valeurs.

*Example :*
```js
//  Égalité simple (convertit les types) 
let a = ("2" == 2);    // true  (Les valeurs se ressemblent)
let b = ("2" != 2);    // false (Ils ne sont pas différents en valeur)
```

- `Egalité stricte (===)` : Compare à la fois la **valeur** ET le **type** de la donnée (texte, nombre, etc.).

*Bonne pratique : Prenez l'habitude de toujours utiliser l'égalité stricte (=== et !==). Cela permet d'éviter de nombreux bugs et erreurs inattendues dans votre code !*

*Example :*

```js

// Égalité stricte (vérifie le type ET la valeur)
let c = ("2" === 2);   // false (L'un est du texte, l'autre est un nombre !)
let d = ("2" !== 2);   // true  (Ils sont bien strictement différents)
```

### d. Opérateurs de comparaison
Tout comme en mathématiques, les opérateurs de comparaison fonctionnent de la même manière que dans la plupart des autres langages de programmation.

*Note: ces opérateurs peuvent également être utilisés pour comparer du texte (chaînes de caractères) selon l'ordre alphabétique.*

[Opérateur de comparaison](../Images/OperateurComparaison.png) 

*Example:*

```js
// Comparaison de nombres 
let a = (2 > 2);          // false (Strictement supérieur)
let b = (2 <= 2);         // true  (Inférieur ou égal)
let d = (2 < 2);          // false (Strictement inférieur)
let e = (2 <= 2);         // true  (Inférieur ou égal)

// Comparaison avec conversion (texte vs nombre) 
let c = ("2" >= 2);       // true  (Le texte "2" est converti en nombre pour comparer)

// Comparaison de texte (ordre alphabétique) 
let f = ('abc' < 'def');  // true  (La lettre 'a' vient avant 'd' dans l'alphabet)
```

### e. Opérateurs logiques

- `ET (&&)` : La condition entière n'est vraie que si toutes les sous-conditions sont vraies.

*Example:*

```js
if (x < y && x > 3) { /* ... */ } // Vrai seulement si x est à la fois PLUS PETIT que y ET PLUS GRAND que 3.
```

- `OU (||)` : La condition entière est vraie si au moins une des sous-conditions est vraie.

*Example:*

```js
if (x < y || x > 5) { /* ... */ } // Vrai si x est PLUS PETIT que y OU PLUS GRAND que 5.
```


## 4.Statements
### a. Conditions
Les conditions permettent d'exécuter du code seulement si une affirmation est vraie. On utilise les mots-clés if, else if, et else.
- if / else
### b. Boucles
Les boucles servent à répéter une action sans avoir à réécrire le code.
- For
- While

- Switch



## 5.Functions















## 3. Écrire des fonctions

<!-- termynal -->

```
# Forme classique
> function calculerTotalHT(prix, quantite) { return prix * quantite }
undefined
> calculerTotalHT(45, 3)
135
# Forme fléchée, plus courte
> const calculerTTC = (montant) => montant * 1.2
undefined
> calculerTTC(135)
162
```

---

## 4. Les blocs

<!-- termynal -->

```
$ cat bloc.js
if (true) {
  const message = "Bonjour";
  console.log(message);
}
console.log(message);
$ node bloc.js
Bonjour
ReferenceError: message is not defined
# La variable n'existe qu'entre les accolades qui l'entourent
```




# Quiz – Atelier 1

<!-- mkdocs-quiz intro -->

<quiz>
Quel mot-clé utilise-t-on pour une valeur qui ne changera jamais ?

- [x] `const`
- [ ] `let`
- [ ] `var`
- [ ] `final`

En JavaScript moderne, la règle est : `const` par défaut, `let` uniquement quand la valeur doit être modifiée. `var` est l'ancienne syntaxe, on ne l'utilise plus.
</quiz>

<quiz>
Que vaut `typeof "45"` ?

- [ ] `'number'`
- [x] `'string'`
- [ ] `'text'`
- [ ] `45`

Les guillemets font toute la différence : `45` est un nombre, `"45"` est une chaîne de caractères contenant deux chiffres.
</quiz>

<quiz>
Qu'affiche `console.log("Prix : " + 45)` ?

- [ ] `45`
- [x] `Prix : 45`
- [ ] `Prix : 45` avec une erreur
- [ ] `NaN`

Dès qu'un des deux opérandes est une chaîne, le `+` ne fait plus une addition mais une **concaténation** : le nombre est converti en texte.
</quiz>

<quiz>
Quels types font partie des types de base de JavaScript ?

- [x] `number`
- [x] `string`
- [x] `boolean`
- [ ] `integer`

JavaScript ne distingue pas les entiers des décimaux : tout est `number`. Les autres types de base sont `undefined`, `null`, `symbol` et `bigint`.
</quiz>

<quiz>
Que manque-t-il à cette fonction pour être utilisable dans un calcul ?

```js
function calculerTotal(prix, quantite) {
  console.log(prix * quantite);
}
```

- [ ] Rien, elle est correcte
- [x] Un `return` à la place du `console.log`
- [ ] Un point-virgule
- [ ] Le mot-clé `const`

Elle affiche le résultat mais ne le **renvoie** pas : `calculerTotal(45, 3) * 1.2` donnerait `NaN`. Une fonction de calcul retourne une valeur, elle n'affiche rien.
</quiz>

<quiz>
Qu'affiche ce code ?

```js
if (true) {
  const message = "Bonjour";
}
console.log(message);
```

- [ ] `Bonjour`
- [ ] `undefined`
- [x] Une erreur : `message is not defined`
- [ ] Rien du tout

Une variable déclarée avec `const` ou `let` n'existe qu'à l'intérieur de son bloc, c'est-à-dire entre les accolades qui l'entourent. En dehors, elle n'existe plus.
</quiz>

<quiz>
La forme courte pour écrire une fonction, avec le symbole `=>`, s'appelle une fonction [[fléchée]].

Exemple : `const doubler = (n) => n * 2;`
</quiz>

<!-- mkdocs-quiz results -->




# TEST - Atelier 1 – Découvrir les bases de JavaScript

!!! info "En bref"
    **Durée : 15 min** · **Prérequis :** Node.js installé · **Fichier :** `atelier1.js`
    · **Exécution :** `node atelier1.js`

## Objectif

Créer une petite fiche produit pour une boutique, en manipulant les quatre
briques de base du langage : **variables**, **types**, **fonctions**, **blocs**.

Créez un fichier `atelier1.js` et avancez partie par partie. Après chaque
partie, relancez `node atelier1.js` pour vérifier que tout fonctionne encore.

---

## Partie 1 — Déclarer des variables (3 min)

Déclarez trois variables :

- `nomProduit` : le nom du produit, une chaîne de caractères. Il ne changera
  jamais, donc utilisez `const`.
- `prixHT` : le prix hors taxes, un nombre. Il pourra changer : utilisez `let`.
- `quantite` : la quantité commandée, un nombre, en `let` également.

Affichez-les avec `console.log()`.

??? success "Corrigé"
    ```js
    const nomProduit = "Clavier";
    let prixHT = 45;
    let quantite = 3;

    console.log(nomProduit, prixHT, quantite);
    ```
    Règle simple à retenir : **`const` par défaut, `let` seulement si la valeur
    doit changer.** On n'utilise plus `var` en JavaScript moderne.

---

## Partie 2 — Observer les types (4 min)

JavaScript ne demande pas de déclarer le type d'une variable : il le déduit.
L'opérateur `typeof` permet de le vérifier.

1. Affichez le type de chacune de vos trois variables.
2. Ajoutez `console.log(typeof true);` et `console.log(typeof rienDuTout);`
   (une variable jamais déclarée).
3. Testez enfin ces deux lignes et comparez le résultat :

```js
console.log(prixHT + quantite);
console.log("Prix : " + prixHT);
```

Que s'est-il passé sur la deuxième ligne ?

??? success "Corrigé"
    Les types affichés sont `string`, `number`, `number`, `boolean`, puis
    `undefined`.

    La première ligne fait une addition (`48`), la seconde une **concaténation**
    (`Prix : 45`). Le signe `+` change de sens dès qu'une chaîne est en jeu : il
    convertit alors le nombre en texte. C'est la source d'erreur la plus
    fréquente chez les débutants.

---

## Partie 3 — Écrire des fonctions (5 min)

Écrivez deux fonctions, chacune sous une forme différente :

| Fonction | Forme | Rôle |
| -------- | ----- | ---- |
| `calculerTotalHT(prix, quantite)` | déclaration `function` | renvoie `prix × quantite` |
| `calculerTTC(montant)` | fonction fléchée `=>` | renvoie le montant avec 20 % de TVA |

Attention : vos fonctions doivent **renvoyer** (`return`) une valeur, pas
l'afficher. C'est l'appelant qui décide quoi en faire.

Testez avec vos variables : le total HT doit valoir `135` et le TTC `162`.

??? success "Corrigé"
    ```js
    function calculerTotalHT(prix, quantite) {
      return prix * quantite;
    }

    const calculerTTC = (montant) => montant * 1.2;

    console.log(calculerTotalHT(prixHT, quantite));           // 135
    console.log(calculerTTC(calculerTotalHT(prixHT, quantite))); // 162
    ```
    Les deux formes font la même chose. La fonction fléchée est simplement une
    écriture plus courte, très répandue dans le code moderne.

---

## Partie 4 — Comprendre les blocs (3 min)

Un **bloc** est tout ce qui se trouve entre `{` et `}`. Une variable déclarée
avec `let` ou `const` n'existe qu'à l'intérieur de son bloc.

Testez ce code et observez l'erreur :

```js
if (quantite > 0) {
  const message = "Commande valide";
  console.log(message); // fonctionne
}

console.log(message); // ?
```

Corrigez-le pour que l'affichage final fonctionne, **sans supprimer le `if`**.

??? success "Corrigé"
    La dernière ligne lève `ReferenceError: message is not defined` : `message`
    est mort en même temps que le bloc `if`.

    On déclare la variable **avant** le bloc :

    ```js
    let message = "Commande vide";

    if (quantite > 0) {
      message = "Commande valide";
    }

    console.log(message);
    ```

---

## Partie 5 — Assembler (bonus, si le temps le permet)

Écrivez une fonction `afficherFiche()` qui utilise tout ce qui précède et
affiche exactement :

```text
Clavier — 3 x 45 € = 135.00 € HT (162.00 € TTC)
```

Indice : `montant.toFixed(2)` formate un nombre avec deux décimales.

??? success "Corrigé"
    ```js
    function afficherFiche() {
      const totalHT = calculerTotalHT(prixHT, quantite);
      const totalTTC = calculerTTC(totalHT);
      console.log(
        `${nomProduit} — ${quantite} x ${prixHT} € = ${totalHT.toFixed(2)} € HT (${totalTTC.toFixed(2)} € TTC)`
      );
    }

    afficherFiche();
    ```
    Les backticks ` `` ` créent un *template literal* : on y insère des valeurs
    avec `${...}`, sans concaténation.

---

## Ce que vous devez savoir faire en sortant

- [ ] Déclarer une variable avec `const` ou `let` et choisir entre les deux.
- [ ] Vérifier le type d'une valeur avec `typeof`.
- [ ] Expliquer pourquoi `"Prix : " + 45` ne donne pas un nombre.
- [ ] Écrire une fonction qui `return` un résultat, sous deux formes.
- [ ] Dire où commence et où finit la vie d'une variable de bloc.
