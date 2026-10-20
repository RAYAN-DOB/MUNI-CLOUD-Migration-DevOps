#!/usr/bin/env python3
"""Authorized lab HTTP probe. Sequential requests, raw latency measurements."""
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from time import perf_counter
from urllib.error import URLError
from urllib.request import urlopen


def percentile(values, rank=0.95):
    """Nearest-rank percentile for non-empty observations."""
    if not values:
        raise ValueError("At least one observation required")
    import math
    ordered = sorted(values)
    return ordered[max(0, math.ceil(rank * len(ordered)) - 1)]


def collect(url, count=30, timeout=5.0):
    if count < 1 or count > 10000:
        raise ValueError("count must be between 1 and 10000")
    observations = []
    for iteration in range(1, count + 1):
        started = perf_counter()
        status = "failed"
        try:
            with urlopen(url, timeout=timeout) as response:
                response.read()
                status = str(response.status)
        except (URLError, OSError) as err:
            status = type(err).__name__
        latency_ms = (perf_counter() - started) * 1000
        observations.append((iteration, status, round(latency_ms, 3)))
    return observations


def main():
    parser = argparse.ArgumentParser(description="Mesure latence HTTP en lab autorisé")
    parser.add_argument("--url", default="http://127.0.0.1:8080/health")
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--output", default="results/latency.csv")
    args = parser.parse_args()
    results = collect(args.url, args.count, args.timeout)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with out.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["utc_timestamp", "url", "iteration", "http_status", "latency_ms"])
        for iteration, status, latency in results:
            writer.writerow([timestamp, args.url, iteration, status, latency])
    good = [ms for _, status, ms in results if status.startswith("2")]
    print(f"URL: {args.url} | total={len(results)} | succès={len(good)} | échecs={len(results)-len(good)}")
    if good:
        print(f"médiane={median(good):.2f}ms | p95={percentile(good):.2f}ms")
    print(f"CSV: {out}")
    return 0 if len(good) == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
