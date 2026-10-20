#!/usr/bin/env sh
# Affiche une photographie de ressources de VM Linux.
# Un échantillon ponctuel n'est PAS un benchmark représentatif.
set -eu
echo "=== MUNI-CLOUD VM snapshot / $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo "Hostname: $(hostname)"
uname -sr
echo "--- Memory (kB) ---"
grep -E '^(MemTotal|MemFree|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
echo "--- CPU cores ---"
getconf _NPROCESSORS_ONLN
echo "--- Disk root ---"
df -h /
echo "--- Uptime ---"
uptime
echo "--- Optional Docker containers ---"
if command -v docker >/dev/null 2>&1; then
  docker ps --format '{{.Names}};{{.Image}};{{.Status}}' || true
else
  echo "Docker non installé (attendu pour baseline VM)."
fi
