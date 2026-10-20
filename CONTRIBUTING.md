# Guide de contribution — Groupe 8
1. Ouvrir/choisir une carte Trello et un ticket GitHub avec critère d'acceptation.
2. Créer une branche : **feature/numero-description** ou **docs/numero-description**.
3. Faire un petit commit descriptif ; pas de fichiers de données sensibles ou secrets.
4. Lancer **python3 -m unittest discover -s tests -v** et **docker compose config --quiet**.
5. Ouvrir une Pull Request vers **main**, lier le ticket, ajouter captures et plan de retour arrière si nécessaire.
6. Faire relire par un autre membre ; n'intégrer que si les tests passent et l'impact est compris.
7. Ne jamais intervenir sur une VM de production sans autorisation écrite et fenêtre de maintenance.
8. La « définition de terminé » exige test, documentation, revue et preuve.
