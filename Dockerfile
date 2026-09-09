# ---------- builder ----------
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc=4:12.2.0-3 \
        build-essential=12.9 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir \
        pip==25.0.1 \
        wheel==0.45.1 \
    && python -m pip wheel \
        --no-cache-dir \
        --wheel-dir=/wheels \
        -r requirements.txt

# ---------- runtime ----------
FROM python:3.11-slim-bookworm AS runtime

WORKDIR /app

ENV FLASK_APP=app.py

COPY --from=builder /wheels /wheels
COPY requirements.txt ./

RUN python -m pip install \
        --no-cache-dir \
        --no-index \
        --find-links=/wheels \
        -r requirements.txt \
    && rm -rf /wheels

COPY . .

CMD ["python", "app.py"]
