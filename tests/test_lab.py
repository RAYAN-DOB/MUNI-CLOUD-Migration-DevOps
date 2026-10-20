from pathlib import Path
import unittest


class LabFilesTests(unittest.TestCase):
    def test_three_service_pilot_files_present(self):
        root = Path(__file__).resolve().parents[1]
        for rel in ("lab/compose.pilotes.yaml", "lab/intranet/index.html",
                    "lab/wiki/index.html", "Dockerfile"):
            self.assertTrue((root / rel).is_file(), rel)

    def test_no_claim_of_real_municipal_data(self):
        root = Path(__file__).resolve().parents[1]
        for rel in ("lab/intranet/index.html", "lab/wiki/index.html"):
            text = (root / rel).read_text()
            self.assertIn("ficti", text.lower())


if __name__ == "__main__":
    unittest.main()
