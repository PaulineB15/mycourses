# JavaScript Basis

JavaScript (JS) : est un langage de programmation côté client. Il permet de rendre les
pages web interactives et dynamiques (modifier le contenu, réagir aux clics, animer des
éléments) sans avoir besoin de recharger la page.


## Basic syntax
- JavaScript is case-sensitive. Lines end by `;`
 - Block are delimited curly brackets by `{ }`
 - Comments are between `/* */` for multiple lines or after `//` for one line.

## Variables & Types

### Declare a variable with:
- `Const` - Valeur qui ne change pas
- `Let` - Valeur qui change

*Example :*

```js
const firstName = "Pauline"; 
let age = 38;                 
let etudiante = true;        
```

### Types
- `String`- Text that is wrap it in `''`or `""`
- `Number`- 2 types of numbers: `integer (30)` and `floating (5.2)`
- `Boolean`- To test a condition `(true of false)`
- `null or undefined`- Both null and undefined are used for absence of a value. One is used when the variable has been initialiazed : null. The other one is used when the variable has not been initialized : undefined. It can be returned by function that have no return statement.

*Example :*

```js
let welcomeMessage = "Hello Pauline !"; // String (Chaîne de caractère) 
let age = 38;                          // Number 
let etudiante = true;                 // Boolean (true/false)
```

### Other types
- `Array` - Liste ordonnée -
contains multiple values enclosed in square brackets and separated by commas
- `Object` - Ensemble de propriétés (clé: valeur)
n object is a structure of code that models a real-life object. You can have an object that represents a box and contains information about its width, length, and height, or you could have an object that represents a person, and contains data about their name, height, weight, what language they speak, how to say hello to them, and more

*Example :*

```js
let skills = ["HTML","CSS"];            // Array
let user = {
    name:"Pauline",
    age: 38,
    school:"La Fabrique du Numérique 41}; // Object
```


## Operators 
Pour prendre des décisions dans le code
- === Egalité stricte (vérifie la valeur ET le type).
- !== Différent de.
- < > Plus eptit, plus grand.

### Arithmetic
Arithmetic operators are used for performing mathematical calculations in JavaScript.

![Arithmetic operators](../Images/ArithmeticOperators.png)

### Equality
### Comparison

## Statements
## Functions

[def]: ./Images/Arithmeticoperators