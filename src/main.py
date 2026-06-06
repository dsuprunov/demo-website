import os
import socket
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from datetime import datetime, timezone


app = FastAPI()


@app.get("/", response_class=JSONResponse)
def root(request: Request):
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "server_name": os.environ.get("HOSTNAME") or socket.gethostname(),
        "server_address": ":".join(map(str, request.scope.get("server"))),
        "uri": request.url.path,
        "app_color": os.environ.get("APP_COLOR", "unknown"),
        "app_version": os.environ.get("APP_VERSION", "unknown"),
        "image_tag": os.environ.get("IMAGE_TAG", "unknown"),
    }


@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "OK"
