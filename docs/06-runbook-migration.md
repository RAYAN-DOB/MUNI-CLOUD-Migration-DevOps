# 06 — Procédure de migration et retour arrière
**Pour environnement de laboratoire uniquement**. Adapter et faire approuver par le tuteur avant toute utilisation réelle.

## A. Qualification et préparation
1. Identifier le service, sa licence, OS, ports, dépendances, stockage, exigences disponibilité.
2. Définir la version source, les données à conserver, les cas de test et seuils de service.
3. Inventorier la VM avant migration (CPU/RAM/disque alloué et consommé, mises à jour, routes).
4. Mesurer l'état **AVANT** au repos et sous charge reproductible (cf. 07-metrologie).
5. Sauvegarder configurations et données ; **restaurer dans un test isolé**. Un snapshot seul ne suffit pas pour bases.
6. Préparer image officielle/de confiance, volumes persistants, secrets hors dépôt, scan et healthcheck.

## B. Migration pilote
1. Déployer Docker dans une VM Linux Proxmox dédiée.
2. Configurer réseau Docker et reverse proxy ; ne pas exposer de ports d'administration.
3. Exporter/importer les données de test en respectant versions, schéma et cohérence.
4. Démarrer le conteneur, lancer tests santé, fonctionnels, authentification et sécurité.
5. Bascule sur le service **non critique** après décision de l'équipe.
6. Documenter durée de bascule, commandes et incidents.
7. Mesurer l'état **APRÈS** avec même charge et même protocole. Conserver la VM témoin jusqu'à recette.

## C. Contrôles post-bascule
- /health répond ; routes et TLS OK ; données présentes et permissions correctes.
- Logs et statut des conteneurs consultés ; pas de secrets dans logs.
- Sauvegarde conteneur testée, restauration contrôlée, retour arrière chronométré.
- Runbook versionné et validé avec preuve anonymisée.

## D. Retour arrière si incident
**Déclencheurs** : santé rouge, perte fonctionnelle, données incohérentes, sécurité compromise ou délai maximal de bascule dépassé.
1. Geler les écritures / désactiver le nouveau service pour éviter la divergence.
2. Réactiver l'ancienne VM isolée et vérifier intégrité/compatibilité des données.
3. Restaurer le routage ou l'entrée reverse proxy vers l'ancienne VM.
4. Exécuter la recette, confirmer retour avec responsable, ouvrir ticket d'incident.
5. **Attention** : en présence d'écritures nouvelles, le retour demande un plan de réconciliation des données, pas une simple remise en route de l'ancienne VM.

## E. Fiche de changement
- Ticket, responsable, approbation DSI si réel, créneau, périmètre, dépendances.
- Version avant/après, lien PR, sauvegarde identifiée hors GitHub.
- Journal début/fin, résultats, signature de recette, incidents, décision de clôture.
