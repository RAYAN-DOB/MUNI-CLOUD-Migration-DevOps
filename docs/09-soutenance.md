# 09 — Recette, démonstration jury et dossier final
## Démonstration 10–12 minutes (à ajuster à la durée officielle)
1. **1 min** : besoins mairie de 300 agents fictifs ; périmètre pilote et risques.
2. **2 min** : schéma avant/après, choix de Docker dans une VM Proxmox.
3. **3 min** : service web témoin fonctionnel, conteneur Docker, healthcheck, sauvegarde.
4. **2 min** : modifier une ligne du portail, créer une PR, montrer CI ; si staging configuré, push sur main après validation et nouvelle version déployée.
5. **2 min** : tableau des valeurs RAM/CPU/temps avant/après et interprétation honnête.
6. **1–2 min** : risques, rollback testé, contribution des 4 membres et bilan.

## Scénario plan B
Si connexion Internet/GitHub indisponible : lancer en local via Docker Compose et montrer captures horodatées du dernier workflow + vidéo de déploiement. Bien dire que ce sont des preuves enregistrées et non du direct.

## Recette minimale
- [ ] VM et conteneur démarrent à partir de la documentation.
- [ ] /health == HTTP 200 et le portail s'affiche.
- [ ] Tests unitaires et build CI verts.
- [ ] Accès administration isolé, pas de secrets dans Git.
- [ ] Persistance des données pilote vérifiée.
- [ ] Restauration et rollback exécutés dans le lab.
- [ ] 3 essais comparables, données avant/après conservées.
- [ ] Problèmes et limites explicités.
- [ ] Chaque étudiant présente une réalisation, un obstacle et une solution.

## Dossier remis
Rapport projet, cahier des charges, inventaire anonymisé, planning, RACI, registre des risques, architecture Mermaid, captures de tests, données brutes benchmark, fiches de changement, procédure de retour arrière, bilan, liens GitHub/Trello.
