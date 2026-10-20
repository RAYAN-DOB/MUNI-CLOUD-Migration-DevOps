#!/usr/bin/env python3
"""Small controlled load test for an AUTHORIZED lab endpoint, not production."""
import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from urllib.parse import urlsplit
from urllib.request import urlopen
from urllib.error import URLError

from scripts.benchmark_http import percentile


def is_local_target(url):
    p = urlsplit(url)
    return p.scheme in ("http", "https") and p.hostname in {"localhost", "127.0.0.1", "::1"}


def one_request(url, timeout):
    start = perf_counter()
    try:
        with urlopen(url, timeout=timeout) as response:
            response.read()
            status = str(response.status)
    except (URLError, OSError) as error:
        status = type(error).__name__
    return status, round((perf_counter() - start) * 1000, 3)


def main():
    p = argparse.ArgumentParser(description="MUNI-CLOUD charge contrôlée sur laboratoire autorisé")
    p.add_argument("--url", default="http://127.0.0.1:8080/health")
    p.add_argument("--requests", type=int, default=300)
    p.add_argument("--workers", type=int, default=10)
    p.add_argument("--timeout", type=float, default=5.0)
    p.add_argument("--output", default="results/load.csv")
    p.add_argument("--allow-remote-lab", action="store_true",
                   help="Cible non locale seulement si autorisation explicite obtenue")
    args = p.parse_args()
    if not is_local_target(args.url) and not args.allow_remote_lab:
        p.error("Cible non locale refusée : utiliser uniquement un laboratoire explicitement autorisé")
    if not 1 <= args.requests <= 10000 or not 1 <= args.workers <= 25 or args.timeout <= 0:
        p.error("Valeurs permises : 1..10000 requêtes, 1..25 workers et délai > 0")
    started = perf_counter()
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(one_request, args.url, args.timeout) for _ in range(args.requests)]
        for future in as_completed(futures):
            results.append(future.result())
    elapsed = max(0.001, perf_counter() - started)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    at = datetime.now(timezone.utc).isoformat()
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["timestamp_utc", "url", "status", "latency_ms"])
        for status, ms in results:
            writer.writerow([at, args.url, status, ms])
    good = [ms for status, ms in results if status.startswith("2")]
    print(f"Requêtes: {len(results)}, erreurs: {len(results)-len(good)}, débit: {len(results)/elapsed:.1f} req/s")
    if good:
        print(f"p95 réponse réussie: {percentile(good):.2f} ms")
    print(f"Fichier: {path}")
    return 0 if len(good) == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
