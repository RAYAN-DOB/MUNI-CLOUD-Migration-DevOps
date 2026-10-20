# Trois services fictifs : baseline VM et cible Docker
Ce dossier fournit un **lab minimal de 3 services reproductibles**, représentant une mini-infrastructure municipale fictive. Il n'y a **aucune donnée réelle**.

## Avant (témoins)
Sur **trois VM Debian distinctes** préparées dans Proxmox (ou les mêmes services isolés pour un test local préliminaire) :
1. VM web : recopier le dossier lab/intranet, puis lancer :

       python3 -m http.server 8081 --bind 127.0.0.1 --directory intranet

2. VM wiki : recopier lab/wiki puis lancer :

       python3 -m http.server 8082 --bind 127.0.0.1 --directory wiki

3. VM application : recopier app/, puis lancer :

       python3 app/server.py

**Important** : avec l'adresse 127.0.0.1, les services ne sont visibles que localement ; SSH/tunnel pour les mesurer à distance. Pour la baseline réelle, installer chacun comme service systemd avec droits minimaux, pas depuis une session shell manuelle. Ne pas exposer les serveurs HTTP Python sur un réseau public : ils sont exclusivement destinés au lab.

## Après (cible)
Dans une **unique VM Debian Docker** :

    docker compose -f lab/compose.pilotes.yaml up -d --build
    docker compose -f lab/compose.pilotes.yaml ps
    curl -fsS http://127.0.0.1:8080/health
    curl -fsS http://127.0.0.1:8081/
    curl -fsS http://127.0.0.1:8082/

Ports locaux VM : 8080 = application de démonstration, 8081 = intranet statique, 8082 = wiki fictif statique.

Les deux pages HTML statiques sont volontairement une **maquette simplifiée** et ne représentent pas la migration de BookStack ou d'un véritable applicatif métier avec base de données. Un wiki dynamique sera un bonus séparé, soumis à audit de compatibilité et tests de sauvegarde.

## Faire une vraie comparaison
- Exécuter exactement la même version du code dans les VM témoins et en conteneurs.
- Même hyperviseur, hôte, charge, quotas et protocole réseau.
- Comparer toutes les VM du scénario AVANT avec la VM Docker et ses conteneurs APRÈS.
- Mesurer le repos et plusieurs niveaux de charge, au moins 3 essais et consigner la méthode.
- Conserver les résultats honnêtes même si la cible consomme plus ou performe moins bien.

## Sécurité / limites
Aucun service réseau municipal réel, aucun accès agent, aucune donnée confidentielle. Seule la préproduction de laboratoire est autorisée.
