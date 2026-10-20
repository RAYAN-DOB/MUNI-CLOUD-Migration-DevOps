# 03 — Diagramme de Gantt
**Hypothèse non validée :** 8 semaines du 26/10/2026 au 18/12/2026. Décaler les dates lorsque la date de soutenance est connue. Jalons et dépendances à adapter selon le tuteur.

```mermaid
gantt
    title MUNI-CLOUD — planning prévisionnel Groupe 8
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    excludes weekends
    section Gouvernance
    Charte et choix du pilote          :a1, 2026-10-26, 5d
    Cahier des charges et inventaire   :a2, after a1, 5d
    section Infrastructure
    VM témoins et mesures T0           :b1, after a1, 10d
    Architecture réseau et sauvegardes :b2, after a2, 10d
    section Containerisation
    Dockerisation du pilote            :c1, after b1, 7d
    Intégration et recette             :c2, after c1, 5d
    section CI/CD & sécurité
    Automatisation en préproduction    :d1, after c1, 6d
    Sécurité et rollback               :d2, after d1, 4d
    section Mesures & jury
    Benchmark avant/après              :e1, after c2, 5d
    Dossier et soutenance              :e2, after e1, 5d
```

## Jalons
- J1 (fin S2) : cadrage et infrastructure témoin validés.
- J2 (fin S4) : au moins un service Docker équivalent, fonctionnel.
- J3 (fin S6) : pipeline staging validé, stratégie de rollback testée.
- J4 (fin S8) : résultats mesurés, bilan et soutenance.

## Rythme
- Point quotidien asynchrone sur Trello/GitHub (blocages).
- Réunion 2 fois/semaine : 15 à 25 minutes ; compte rendu versionné.
- Revue de sprint en fin de chaque quinzaine ; décisions consignées.

Règle : une tâche ne passe dans « Terminé » qu'avec preuve, test et validation d'un autre membre.
