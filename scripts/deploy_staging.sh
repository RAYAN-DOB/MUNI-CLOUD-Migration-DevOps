#!/usr/bin/env sh
# Usage: MUNI_IMAGE=ghcr.io/...:sha-FULLSHA sh scripts/deploy_staging.sh
# Staging only. Configure Docker login, folder and backup before running.
set -eu
: "${MUNI_IMAGE:?Spécifier MUNI_IMAGE avec un tag sha-immuable}"
case "$MUNI_IMAGE" in
  ghcr.io/*:sha-*) ;;
  *) echo "Refus : tag immuable sha- attendu" >&2; exit 2 ;;
esac
echo "Déploiement PREPRODUCTION : $MUNI_IMAGE"
docker compose -f compose.staging.yaml config --quiet
docker compose -f compose.staging.yaml pull
docker compose -f compose.staging.yaml up -d
docker compose -f compose.staging.yaml ps
echo "Vérifier /health via tunnel ou proxy privé ; retour arrière = ancienne valeur MUNI_IMAGE"
