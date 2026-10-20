# MUNI-CLOUD — Migration & DevOps
**Groupe 8 | Projet pédagogique | Mairie fictive d'environ 300 agents**

[![CI](https://github.com/RAYAN-DOB/MUNI-CLOUD-Migration-DevOps/actions/workflows/ci.yml/badge.svg)](https://github.com/RAYAN-DOB/MUNI-CLOUD-Migration-DevOps/actions/workflows/ci.yml)

## 🎯 Objectif
Étudier puis expérimenter **la migration progressive de services de VM vers des conteneurs Docker, hébergés dans une VM Proxmox**, avec sécurisation, sauvegardes, déploiement automatisé **en préproduction** et comparaison objective des performances avant/après.

**Statut : conception et laboratoire.** Aucune migration de production, économie de ressources ni disponibilité du CI/CD ne sont actuellement prouvées. Les services et données du lab sont fictifs.

| Équipe | Contribution proposée (à valider) |
| --- | --- |
| Rayan DOB | Coordination, développement applicatif et CI/CD |
| Dylan TONIOLO | Virtualisation, Linux et migration |
| Wissam BOUDOUR | Réseau, sécurité, sauvegardes |
| Tom HARDY | Métrologie, tests, qualité et bilan |

**Tableau de gestion du groupe** : https://trello.com/b/ZGU2KZX8/groupe-8-muni-cloud-migration-devops

## 🧭 Navigation
- [Cadrage et critères de succès](docs/01-cadrage.md)
- [Architecture avec schémas Mermaid](docs/02-architecture.md)
- [Planning de Gantt (8 semaines indicatives)](docs/03-gantt.md)
- [Matrice RACI](docs/04-raci.md) et [risques](docs/05-risques.md)
- [Procédure de migration & rollback](docs/06-runbook-migration.md)
- [Protocole de mesures et bilan avant/après](docs/07-metrologie.md)
- [Pipeline, sécurité et mise en service](docs/08-devops.md)
- [Soutenance et recette](docs/09-soutenance.md)
- [Backlog & répartition](docs/10-backlog.md)
- [Budget, communication et gouvernance](docs/11-gouvernance.md)
- [Modèles de fichiers](templates/) et [scripts](scripts/)
- [Politique de sécurité](SECURITY.md) · [Contributions](CONTRIBUTING.md)

## 🧱 Laboratoire technique
- **Avant** : un service par VM Debian de référence (à déployer et mesurer réellement).
- **Après** : mêmes services conteneurisés dans **une VM Debian Docker sur Proxmox**, volumes persistants, segmentation réseau.
- **Démo fournie** : portail web Python standard library (aucune dépendance pip), une image Docker, une suite de tests et un pipeline CI.
- **Services pilotes candidats** : intranet de démonstration, wiki de laboratoire et une petite API. Rien n'est présumé migrable en production sans audit.

## 🚀 Lancer immédiatement le portail
Prérequis : Docker Engine + plugin Docker Compose sur une VM Linux de laboratoire (ne pas installer Docker directement sur l'hôte Proxmox).

    git clone https://github.com/RAYAN-DOB/MUNI-CLOUD-Migration-DevOps.git
    cd MUNI-CLOUD-Migration-DevOps
    docker compose up -d --build
    docker compose ps
    curl -fsS http://127.0.0.1:8080/health

Accès **local à la VM** : http://127.0.0.1:8080
Depuis ton PC : tunnel SSH sécurisé :

    ssh -L 8080:127.0.0.1:8080 utilisateur@IP_VM
    # puis ouvrir http://127.0.0.1:8080

Pour les tests sans Docker :

    python3 -m unittest discover -s tests -v
    python3 app/server.py

Le portail est un **prototype pour la soutenance**, pas une interface d'administration Proxmox ni un outil de supervision de production.

## 🔄 CI/CD
- Pull request : tests Python + analyse Compose + construction image Docker.
- Push sur main : publication de l'image de **staging** sur GHCR si les permissions sont disponibles.
- Déploiement distant après push : **désactivé par défaut**, uniquement si la variable GitHub ENABLE_STAGING_DEPLOY=true et les secrets SSH sont configurés. Aucun déploiement de production automatique.
- Voir [procédure DevOps](docs/08-devops.md).

## 📊 Avant / après
Les modèles CSV sont volontairement vides de vrais résultats. Les chiffres doivent être collectés sous conditions comparables, à partir de **3 séries de mesures minimum**, avec mêmes services et charge. Le nombre de VM ne prouve pas à lui seul un gain RAM ou CPU.

## 🔐 Données publiques
**Ce dépôt est PUBLIC.** Ne jamais publier : secrets, identifiants, mots de passe, IP/adresses internes réelles, plans de réseau opérationnels, noms d'agents, dossiers municipaux, sauvegardes, journaux sensibles ou configurations de production. Employer uniquement des jeux fictifs/anonymisés **et autorisés**. Validation du tuteur requise avant toute intervention réelle.

## ✅ Définition de « terminé »
3 services pilotes testés ; équivalence fonctionnelle ; pipeline CI vert ; copie de sauvegarde restaurée ; rollback testé ; benchmarks sourcés ; protocole de recette validé ; documentation et démonstration en direct.
