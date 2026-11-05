import html
import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/")
def index():
    title = html.escape(os.getenv("APP_TITLE", "Laboratorio Docker"))
    color = html.escape(os.getenv("APP_COLOR", "#2563eb"), quote=True)
    version = html.escape(os.getenv("APP_VERSION", "dev"))
    hostname = html.escape(socket.gethostname())
    return f"""<!doctype html><html lang='es'><meta charset='utf-8'>
    <meta name='viewport' content='width=device-width,initial-scale=1'>
    <title>{title}</title><body style='font:18px system-ui;margin:4rem auto;max-width:760px'>
    <h1 style='color:{color}'>{title}</h1>
    <p>Versión de imagen: <b>{version}</b></p>
    <p>Contenedor que respondió: <code>{hostname}</code></p>
    <button onclick='location.reload()'>Otra solicitud</button>
    <p><small>Endpoint de estado: <a href='/health'>/health</a></small></p>
    </body></html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
