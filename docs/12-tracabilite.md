# 12 — Matrice de traçabilité et critères d'acceptation
| Besoin | Livraison / fichier | Vérification | État initial |
|---|---|---|---|
| Présenter le projet | docs/01-cadrage.md | Revue des objectifs | Rédigé, non validé |
| Schéma avant/après | docs/02-architecture.md | Revue architecture | Rédigé, fictif |
| Planifier 8 semaines | docs/03-gantt.md | Gantt conforme au calendrier validé | Provisoire |
| Partager les tâches | docs/04-raci.md, Trello, issues | Réunion d'attribution | Proposé |
| Gérer les risques | docs/05-risques.md | Revue bihebdomadaire | Initialisé |
| Migrer VM → Docker | lab/ et compose.yaml | Recette sur Proxmox | Prototype livré, non déployé |
| Automatiser tests | .github/workflows/ci.yml | Actions verte sur main et PR | Code publié, exécution à vérifier |
| Publier staging | Workflow GitHub, compose.staging.yaml | /health version après push | Non configuré |
| Sécuriser les flux | SECURITY.md et doc architecture | Matrice de flux vérifiée | À réaliser |
| Sauvegarder/restaurer | docs/06-runbook-migration.md | Test de restauration | Non réalisé |
| Comparer ressources | scripts/report.py et mesures.csv | 3 essais et valeurs sources | Script livré, données à collecter |
| Soutenance | docs/09-soutenance.md | Répétition complète | À réaliser |

État « code publié » ne signifie **pas** que les fonctionnalités sont déployées ou testées dans Proxmox. La grille est mise à jour avec des preuves, issues/PR et comptes rendus.
