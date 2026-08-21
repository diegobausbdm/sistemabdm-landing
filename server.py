"""Servidor estático mínimo para el sitio www.sistemabdm.com.ar."""

import http.server
import os

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para deshabilitar caché en HTML
        if self.path.endswith('.html') or self.path == '/':
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        super().end_headers()

port = int(os.environ.get("PORT", 8000))
http.server.test(
    HandlerClass=NoCacheHTTPRequestHandler,
    port=port,
    bind="0.0.0.0",
)
