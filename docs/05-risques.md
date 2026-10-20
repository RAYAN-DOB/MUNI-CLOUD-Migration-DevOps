# 05 — Registre des risques
Barème : probabilité P et impact I de 1 (faible) à 5 (fort). Criticité = P × I. Scores initiaux proposés à réviser en réunion.

| ID | Risque | P | I | Score | Prévention | Réaction |
|---|---|---:|---:|---:|---|---|
| R01 | Service interrompu pendant bascule | 3 | 5 | 15 | Fenêtre validée, healthchecks, test | Retour à VM témoin |
| R02 | Perte de données / volumes | 2 | 5 | 10 | Snapshots + dumps + restauration testée | Restaurer copie vérifiée |
| R03 | Accès admin trop large ou secrets Git | 3 | 5 | 15 | Comptes dédiés, revue, GitHub secrets | Révoquer, remplacer, investiguer |
| R04 | Appli incompatible conteneurs | 3 | 4 | 12 | Audit dépendances et POC tôt | Remplacer candidat |
| R05 | Résultats de benchmark incomparables | 4 | 4 | 16 | Charge, durée, hôte, quotas identiques | Refaire mesures et documenter |
| R06 | Retard / manque de disponibilité | 4 | 3 | 12 | MVP, WIP limité, point 2x/semaine | Réduire à 1 service |
| R07 | CI/CD expose le staging | 2 | 5 | 10 | Pas de prod auto, secrets, SSH limité | Désactiver pipeline, révoquer |
| R08 | Indisponibilité de Proxmox | 3 | 4 | 12 | Snapshots, export configs, solution locale | Rétablir lab et replanifier |

**Escalade :** score ≥ 15 = revue à chaque réunion + propriétaire nommé. Toute action réelle sur une infrastructure municipale requiert la validation de la DSI. Ne jamais charger dans GitHub le détail de risques ou configurations sensibles de production.
