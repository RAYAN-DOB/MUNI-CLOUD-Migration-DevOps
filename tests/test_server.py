import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen

from app.server import Handler


class PortalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def test_health(self):
        with urlopen(self.base + "/health", timeout=5) as resp:
            self.assertEqual(resp.status, 200)
            self.assertEqual(json.load(resp)["status"], "ok")

    def test_info_contains_only_simulated_services(self):
        with urlopen(self.base + "/api/info", timeout=5) as resp:
            data = json.load(resp)
        self.assertEqual(data["project"], "MUNI-CLOUD")
        self.assertEqual(len(data["services"]), 3)
        self.assertTrue(all(s["simulated"] for s in data["services"]))

    def test_portal_loads(self):
        with urlopen(self.base, timeout=5) as resp:
            html = resp.read().decode()
            self.assertIn("MUNI-CLOUD", html)

    def test_unknown_resource_returns_404(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(self.base + "/not-here", timeout=5)
        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
