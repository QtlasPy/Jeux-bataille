<h1> Rapport de projet </h1>

<h2> Introduction :</h2>

<p>Dans le cadre de notre projet en NSI, nous avons modÃ©lisÃ© le jeu de Bataille en utilisant le langage de programmation Python et en utilisant la Programmation OrientÃ©e Objet. </p>

<h2> Analyse du ProblÃ¨me PosÃ© :</h2>

<p> La Bataille possÃ¨de des rÃ¨gles prÃ©cises, on a dÃ» le modÃ©liserÂ : </p>

<ul>
  <li><strong>Joueurs :</strong> Deux joueurs, ayant chacun un paquet de cartes.</li>
  <li><strong>52 Cartes :</strong> Un jeu de 52 cartes, divisÃ© entre les joueurs.</li>
  <li><strong>Paquet de Joueur :</strong> Chaque joueur possÃ¨de un paquet de cartes, oÃ¹ lâ€™on peut tirer et ajouter des cartes.</li>
  <li><strong>Carte :</strong> Les cartes du jeu, codÃ©es une valeur et une figure.</li>
  <li><strong>Partie :</strong> La gestion du dÃ©roulement du jeu, des batailles et de la fin de la partie.</li>
</ul>

<p>GrÃ¢ce Ã  cette analyse on a pu travailler et diviser le projet en plusieurs classes dont chaque personne du groupe a Ã©tÃ© attribuÃ©Â :</p>

<li> Julien : Partie </li>
<li> TimÃ©o : JeuCartes </li>
<li> Laura / Lana : Joueur et Cartes </li>
<li> Charles : Paquet </li>


<h2> Solutions ProposÃ©es :</h2>

<h3> Carte :</h3>

<p>La classe <code>Carte</code> a Ã©tÃ© crÃ©Ã©e pour reprÃ©senter les cartes du jeu. Chaque carte est dÃ©finie par une valeur et une figure. Et il y'a notament une methode afficher qui avec la valeur et la famille renvoie une image de la carte associer.</p>
<h3> Paquet :</h3>

<p>La classe <code>Paquet</code> gÃ¨re les opÃ©rations que lâ€™on fait sur le paquet. Elle utilise une file pour stocker les cartes et possÃ¨de des mÃ©thodes pour ajouter une carte au paquet, obtenir la taille du paquet et afficher le paquet.</p>

<h3> JeuCartes :</h3>

<p>La classe <code>JeuCartes</code> reprÃ©sente l'ensemble du jeu de cartes. Elle initialise les 52 cartes, avec une liste par comphrension, et offre une mÃ©thode pour mÃ©langer le jeu.</p>


<h3> Player :</h3>

<p>La classe <code>Player</code> reprÃ©sente un joueur avec un nom et un paquet de cartes. Elle offre une mÃ©thode pour tirer une carte du paquet.</p>


<h3> Game :</h3>

<p>La classe <code>Game</code> Organise le dÃ©roulement du jeu. Elle initialise le jeu en crÃ©ant un jeu de cartes, distribue les cartes aux joueurs, gÃ¨re les batailles, dÃ©termine le gagnant de la partie et gere toute la partie graphique.</p>

<h3> Graphique : </h3>
<p>A l'aide de la librarie pygame nous avons pue modeliser le jeu en graphique a l'aide d'image de carte. </p>

<h3> Travaille en equipe : </h3>
<p> Ce projet nous a permit d'utiliser un gestionnaire de sauvegarde tel que git grace a sa methode de branche et de mise en commun. </p>

<h2> Conclusion :</h2>

<p> Ce projet nous a permis dâ€™utiliser la PPO dans un contexte rÃ©el. La modÃ©lisation des diffÃ©rents Ã©lÃ©ments de la Bataille nous a permis dâ€™apprendre Ã  structurer un projet efficacement et Ã  travailler en groupe en se rÃ©partissant les tÃ¢ches. </p>


<h2> Lien vers le Code :</h2>

<p> Le code complet du projet est disponible sur notre <a href=https://github.com/QtlasPy/Jeux-bataille> dÃ©pÃ´t GitHub </a.></p>
