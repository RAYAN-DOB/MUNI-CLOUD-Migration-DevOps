#!/usr/bin/env python3
"""Compute honest before/after comparisons from REAL input measurements."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median

FIELDS = ("ram_mb", "cpu_pct", "storage_mb", "deployment_sec", "latency_p95_ms", "rollback_sec")


def relative_change(before, after):
    return None if before == 0 else 100.0 * (after - before) / before


def read_data(path):
    groups = defaultdict(list)
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        expected = {"phase", "service", "trial", *FIELDS}
        if not expected.issubset(set(reader.fieldnames or [])):
            raise ValueError("Invalid CSV headers; see templates/measurements.csv")
        for index, row in enumerate(reader, 2):
            phase = row["phase"].strip().lower()
            if phase not in {"avant", "apres"}:
                raise ValueError(f"Line {index}: phase must be avant/apres")
            service = row["service"].strip()
            if not service:
                raise ValueError(f"Line {index}: service required")
            measures = {}
            for name in FIELDS:
                raw = row[name].strip()
                measures[name] = float(raw) if raw else None
                if measures[name] is not None and measures[name] < 0:
                    raise ValueError(f"Line {index}: {name} cannot be negative")
            groups[(service, phase)].append(measures)
    return groups


def compare(groups, minimum=3):
    services = sorted({service for service, _ in groups})
    results = []
    for service in services:
        before = groups.get((service, "avant"), [])
        after = groups.get((service, "apres"), [])
        if min(len(before), len(after)) < minimum:
            raise ValueError(f"{service}: minimum {minimum} essais dans chaque phase requis")
        for field in FIELDS:
            values_a = [row[field] for row in before if row[field] is not None]
            values_b = [row[field] for row in after if row[field] is not None]
            if not values_a and not values_b:
                continue
            if min(len(values_a), len(values_b)) < minimum:
                raise ValueError(f"{service}/{field}: minimum {minimum} valeurs numériques/phase")
            old, new = median(values_a), median(values_b)
            results.append((service, field, old, new, relative_change(old, new)))
    if not results:
        raise ValueError("No data available")
    return results


def main():
    parser = argparse.ArgumentParser(description="Bilan de migration basé sur données mesurées")
    parser.add_argument("--input", default="templates/measurements.csv")
    parser.add_argument("--minimum", type=int, default=3)
    args = parser.parse_args()
    if args.minimum < 1:
        parser.error("minimum must be positive")
    try:
        report = compare(read_data(args.input), args.minimum)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print("| Service | Indicateur | Avant (médiane) | Après (médiane) | Variation % |")
    print("|---|---|---:|---:|---:|")
    for service, name, old, new, delta in report:
        delta_display = "N/A (avant=0)" if delta is None else f"{delta:+.1f}%"
        print(f"| {service} | {name} | {old:.2f} | {new:.2f} | {delta_display} |")
    print("\nInterprétation : variation négative = réduction de cet indicateur (pas automatiquement une amélioration globale).")


if __name__ == "__main__":
    main()
