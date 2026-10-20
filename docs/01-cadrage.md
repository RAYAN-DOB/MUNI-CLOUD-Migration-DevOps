# 01 — Charte et cahier des charges
**Projet :** MUNI-CLOUD | **Groupe :** 8 | **Contexte :** mairie fictive d'environ 300 agents | **Version :** 0.1 (à valider).

## Besoin
Une DSI souhaite mieux exploiter ses ressources en modernisant des applications hébergées sur plusieurs VM : standardisation, cycles de livraison rapides, sauvegardes fiables, réduction de la charge d'exploitation. Une migration Docker n'est pas toujours adaptée ; elle doit être précédée d'une analyse de compatibilité.

## Problématique
Comment migrer progressivement un périmètre limité d'applications de VM vers des conteneurs sur Proxmox, tout en préservant sécurité, disponibilité, maintenabilité et performance mesurée ?

## Objectifs SMART proposés (indicateurs à vérifier)
1. Sélectionner et documenter **3 services pilotes** avec matrice de dépendances avant fin S2.
2. Migrer au moins **1 service fonctionnellement équivalent en conteneur** à fin S4 ; viser 3 en option selon compatibilité.
3. Obtenir **un pipeline CI vert**, déploiement automatique seulement sur staging à fin S6.
4. Valider au moins **1 restauration et 1 rollback** sur le pilote avant soutenance.
5. Produire **3 répétitions ou plus** de mesures avant/après sous charge comparable, avec données brutes et écarts calculés avant fin S7.
6. Remettre un dossier de projet complet avant fin S8.

**Aucune baisse garantie de RAM/CPU :** les résultats observés peuvent être nuls ou négatifs ; l'analyse doit l'expliquer.

## Périmètre
**Inclus** : VM Debian de labo, Docker Engine/Compose, intranet de démonstration, wiki pilote si éligible, API pilote, pipeline CI, reverse proxy TLS en staging, sécurité minimale, sauvegarde, mesures et soutenance.
**Exclus** : migration d'AD/LDAP, messagerie officielle, applicatifs métier sensibles, données RH, réseaux réels de mairie, accès de production, promesse de haute disponibilité, déploiement automatique en production.

## Parties prenantes
- Étudiants : Dylan TONIOLO, Rayan DOB, Wissam BOUDOUR, Tom HARDY.
- Enseignante : Mme OUBEKKKOU (validation académique à obtenir).
- Tuteur DSI : valide uniquement si l'étude implique des ressources réelles, sans présumer d'une autorisation.
- Utilisateurs fictifs : agents et équipe DSI représentés par des jeux de test.

## Livrables
Charte, WBS/backlog, Gantt, RACI, inventaire, dossiers architecture avant/après, scripts et conteneurs, CI, matrice de flux, plan de migration/rollback, tests, mesures chiffrées, analyse d'écarts, soutenance.

## Critères de recette
- Démarrage via Compose documenté, endpoints / et /health répondent.
- Pipeline tests OK et image construite.
- Services comparés à fonctionnalité et charge égales.
- Restauration et rollback reproductibles.
- Aucun secret ni donnée réelle de mairie publié.
- Contributions des 4 membres traçables par tickets, PR, journal de réunion.

## Hypothèses à confirmer
Durée de 8 semaines, démarrage 26 octobre 2026 et périmètre de 3 services. Budget matériel = laboratoire Proxmox disponible, sous réserve de validation. Ces éléments ne sont pas des engagements ni des données observées.
