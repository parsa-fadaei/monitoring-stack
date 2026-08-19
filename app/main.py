from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"]
)

REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "HTTP request latency",
    ["path"]
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    path = request.url.path

    REQUEST_COUNT.labels(
        method=request.method,
        path=path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        path=path
    ).observe(duration)

    return response


@app.get("/a")
def route_a():
    return {"route": "a"}


@app.get("/b")
def route_b():
    time.sleep(0.2)
    return {"route": "b"}


@app.get("/c")
def route_c():
    time.sleep(0.8)
    return {"route": "c"}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
