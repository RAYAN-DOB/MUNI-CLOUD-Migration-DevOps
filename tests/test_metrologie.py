import unittest

from scripts.benchmark_http import percentile
from scripts.report import compare, relative_change


class CalculationTests(unittest.TestCase):
    def test_percentile(self):
        self.assertEqual(percentile([5, 4, 1, 2, 3]), 5)
        self.assertEqual(percentile([5]), 5)

    def test_relative_change(self):
        self.assertEqual(relative_change(100, 80), -20.0)
        self.assertIsNone(relative_change(0, 8))

    def test_compare_median(self):
        before = [{"ram_mb": v, "cpu_pct": None, "storage_mb": None,
                   "deployment_sec": None, "latency_p95_ms": None,
                   "rollback_sec": None} for v in [100, 120, 110]]
        after = [{"ram_mb": v, "cpu_pct": None, "storage_mb": None,
                  "deployment_sec": None, "latency_p95_ms": None,
                  "rollback_sec": None} for v in [60, 50, 70]]
        report = compare({("service-fictif", "avant"): before,
                          ("service-fictif", "apres"): after})
        self.assertEqual(len(report), 1)
        self.assertEqual(report[0][2], 110.0)
        self.assertEqual(report[0][3], 60.0)

    def test_requires_three_trials(self):
        with self.assertRaises(ValueError):
            compare({("web", "avant"): [{}], ("web", "apres"): [{}]})


if __name__ == "__main__":
    unittest.main()
