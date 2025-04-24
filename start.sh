#!/bin/bash

set -e
export DEBIAN_FRONTEND=noninteractive

echo "🔧 Installazione dipendenze di sistema..."
apt update && apt install -y \
    git wget unzip python3 python3-pip

echo "🐍 Installazione dipendenze Python..."
pip3 install --upgrade pip
pip3 install -r /workspace/imageto3d/requirements.txt

echo "📂 Preparazione directory output..."
mkdir -p /workspace/uploads
mkdir -p /workspace/outputs

echo "🚀 Avvio FastAPI..."
cd /workspace/imageto3d
uvicorn app.main:app --host 0.0.0.0 --port 8000
