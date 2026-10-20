# Sécurité et périmètre autorisé
Ce dépôt est **public** et strictement pédagogique. N'y mettre aucun : mot de passe, jeton, clé SSH, adresse/IP interne d'une vraie mairie, topologie opérationnelle, donnée RH, configuration firewall productive, export de base ou sauvegarde. N'utiliser que des noms et valeurs fictifs dans les exemples.

**Aucune migration réelle sans décision du tuteur DSI**. Audit de dépendances, sauvegarde vérifiée, test de restauration, fenêtre de maintenance, responsable de validation et procédure de retour arrière sont obligatoires.

**Déploiement** : le pipeline cible exclusivement la préproduction. Le job deploy-staging est désactivé tant que ENABLE_STAGING_DEPLOY n'est pas mis à true. Ne jamais placer de secrets GitHub dans des PR, logs ou scripts. Préférer un GitHub Environment « staging » protégé et des comptes SSH non administrateurs.

**Docker** : exécution sans root, permissions minimales, volume persistant pour bases, images mises à jour, TLS reverse-proxy, réseau de management séparé. Aucun accès au socket Docker depuis l'application. Pas de Docker sur l'hyperviseur Proxmox.

**Signalement** : contacter le responsable du dépôt en privé, sans divulguer la vulnérabilité publiquement dans une issue. Révoquer immédiatement tout secret exposé.
