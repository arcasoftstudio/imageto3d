#!/bin/bash

set -e
export DEBIAN_FRONTEND=noninteractive

# ✅ Installa Python e pip
apt update && apt install -y python3 python3-pip unzip

# ✅ Installa dipendenze Python
pip3 install --upgrade pip
pip3 install -r requirements.txt

# ✅ Crea directory se mancano
mkdir -p /workspace/uploads
mkdir -p /workspace/outputs

# ✅ Avvia FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000
