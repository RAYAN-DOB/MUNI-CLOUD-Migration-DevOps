# 08 — GitHub, CI/CD et déploiement de staging
## Fonctionnement du workflow
1. Pull Request : tests unitaires Python, vérification Compose et build Docker.
2. Push validé sur **main** : mêmes tests puis publication d'une image GHCR tag « staging » et d'une version immutable « sha-COMMIT ».
3. Optionnel : déploiement staging si variable GitHub ENABLE_STAGING_DEPLOY définie exactement à true et secrets SSH valides.
4. **Production toujours manuelle**, après validation externe : aucune action du dépôt ne doit déployer automatiquement en production.

## Configurer une VM staging
- VM Debian récente sur Proxmox, Docker Engine et Compose installés et correctifs appliqués.
- Compte dédié sans sudo admin global ; droits Docker = droits élevés, limiter à un compte technique contrôlé.
- Créer le répertoire **/opt/muni-cloud** et placer **compose.staging.yaml**.
- Authentifier GHCR avec token à droits minimaux si package privé ; ou rendre le package de démonstration public après vérification.
- Prévoir une entrée reverse proxy HTTPS, réseau de lab, et accès privé uniquement. Le Compose fourni expose le port **sur loopback 127.0.0.1**.

## Préparer les paramètres GitHub
Créer un environnement GitHub « staging » et 4 secrets :
- STAGING_HOST : hôte de staging autorisé
- STAGING_USER : compte SSH dédié
- STAGING_SSH_KEY : clé privée uniquement pour ce compte
- STAGING_KNOWN_HOSTS : clé d'hôte SSH validée *hors bande*, pas obtenue aveuglément pendant le déploiement

Définir variable **ENABLE_STAGING_DEPLOY=true** uniquement quand le lab est prêt. Laisser false/non définie tant que ce n'est pas le cas.

Pour voir le statut du pipeline : onglet GitHub Actions / « CI - Tests, Docker et image de staging ». Si le package GHCR est invisible, vérifier les permissions de packages du dépôt.

## Vérifier et revenir en arrière
- Vérifier le digest/version et /health.
- Privilégier image « sha-COMMIT » immuable pour une mise en production contrôlée.
- Pour rollback manuel de staging : fixer MUNI_IMAGE dans un fichier .env privé à une **ancienne image validée** puis relancer docker compose -f compose.staging.yaml up -d.
- Un changement de schéma DB exige également un plan de restauration/compatibilité des données.
- Les images Docker ne remplacent pas les sauvegardes de volumes et bases.

## Gouvernance Git
- Branches feature/ID-description.
- PR avec ticket lié, captures anonymisées, tests, relecture.
- Ne pas faire de merge si checks en échec, ni automatiser un déploiement de production après push.
- Demander au propriétaire de configurer Branch Protection / règles d'approbation sur main : l'application GitHub connectée ne possède pas les droits d'administration nécessaires.
