<?php 
$tableau = [1, 2, 3, 4];


// Affichage brut (sans la balise <pre>)
var_dump($tableau);

// Affichage propre (FORTEMENT RECOMMANDÉ)
// En encadrant le var_dump avec la balise HTML <pre>, l'affichage devient indenté et très lisible !
echo "<pre>";
var_dump($tableau);
echo "</pre>";

?>