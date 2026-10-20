# 07 — Métrologie et comparaison avant / après
## Hypothèse à tester
La consolidation de services Docker **peut** réduire une partie du surcoût des OS invités et accélérer les déploiements. Elle peut aussi créer des contentions, régressions ou coûts d'exploitation. La conclusion dépend des mesures.

## Protocole obligatoire
1. Comparer **exactement les mêmes versions et fonctionnalités**, sur le même hyperviseur Proxmox et une allocation comparable.
2. Mesurer les environnements complets (VM Docker comprise) et non seulement la RAM des processus applicatifs.
3. Tester le repos et une charge reproductible, isoler les autres charges et noter versions/quotas.
4. Répéter **au moins trois fois** chaque scénario et utiliser médiane + étendue ou min/max.
5. Chronométrer déploiement complet (du déclencheur à /health vert), arrêt/redémarrage, restauration, rollback.
6. Conserver les mesures brutes horodatées et configuration du test, calculer taux d'échec, p95 latence HTTP, RAM et CPU.
7. Documenter toute modification du matériel ou de la configuration qui limite la comparaison.

## Indicateurs et formules
- Évolution relative (%) = 100 × (après − avant) / avant (si avant ≠ 0).
- « Gain RAM » (%) = 100 × (avant − après) / avant ; positif si réduction.
- Disponibilité (%) = 100 × (durée totale − indisponibilité) / durée totale.
- Temps de déploiement = fin des healthchecks − déclenchement ; choisir même périmètre avant/après.
- Mesure de CPU : préciser unité (pourcentage VM, host ou milliCPU), périmètre et fenêtre.

## Collecter les mesures
Outils possibles : Proxmox métriques VM, /proc/meminfo sur VM, /usr/bin/time, Docker stats, Beszel/Grafana pour courbes. **Exporter les valeurs** dans templates/measurements.csv et conserver captures contextualisées, sans données réelles de mairie.

Exemple de mesure de latence et disponibilité du service pilote (script Python standard library) :

    python3 scripts/benchmark_http.py --url http://127.0.0.1:8080/health --count 30 --output results/latency.csv

Produire le comparatif après saisie de mesures valides :

    python3 scripts/report.py --input templates/measurements.csv

## Modèle de tableau au jury
| KPI | Avant (médiane) | Après (médiane) | Écart | Conclusion |
|---|---:|---:|---:|---|
| RAM totale MB | à mesurer | à mesurer | calculer | |
| CPU moyen % | à mesurer | à mesurer | calculer | |
| Stockage disque MB | à mesurer | à mesurer | calculer | |
| Déploiement sec | à mesurer | à mesurer | calculer | |
| p95 requête ms | à mesurer | à mesurer | calculer | |
| Restauration sec | à mesurer | à mesurer | calculer | |

**Ne jamais inventer ou embellir les données.** Les valeurs d'exemple des maquettes ne sont pas des observations.
