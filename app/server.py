"""MUNI-CLOUD demo portal: stdlib-only HTTP app, fictional data only."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
import json
import os
import time

ROOT = Path(__file__).resolve().parent
STARTED = time.monotonic()
SERVICES = (
    {"name": "Intranet de démonstration", "category": "Web", "phase": "Candidat", "simulated": True},
    {"name": "Wiki documentaire fictif", "category": "Documentation", "phase": "À qualifier", "simulated": True},
    {"name": "API pilote", "category": "Application", "phase": "Laboratoire", "simulated": True},
)


class Handler(BaseHTTPRequestHandler):
    server_version = "MuniCloudLab/0.1"

    def _write(self, status, content_type, payload):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/health":
            body = {"status": "ok", "service": "muni-cloud-lab"}
            self._write(200, "application/json; charset=utf-8", json.dumps(body).encode())
        elif path == "/api/info":
            body = {
                "project": "MUNI-CLOUD",
                "environment": "LAB / données fictives",
                "version": os.environ.get("MUNI_VERSION", "dev"),
                "uptime_seconds": round(time.monotonic() - STARTED),
                "services": SERVICES,
            }
            self._write(200, "application/json; charset=utf-8", json.dumps(body).encode())
        elif path in ("/", "/index.html"):
            self._write(200, "text/html; charset=utf-8", (ROOT / "index.html").read_bytes())
        elif path == "/static/style.css":
            self._write(200, "text/css; charset=utf-8", (ROOT / "static" / "style.css").read_bytes())
        elif path == "/static/app.js":
            self._write(200, "text/javascript; charset=utf-8", (ROOT / "static" / "app.js").read_bytes())
        else:
            self._write(404, "application/json; charset=utf-8", b'{"error":"not_found"}')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    if not (1 <= port <= 65535):
        raise ValueError("PORT must be between 1 and 65535")
    bind_host = os.environ.get("HOST", "0.0.0.0")
    ThreadingHTTPServer((bind_host, port), Handler).serve_forever()
