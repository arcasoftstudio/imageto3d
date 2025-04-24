from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import uuid
import os
from utils.unzip import extract_zip
from app.runner import generate_3d_model

app = FastAPI()

UPLOAD_DIR = "/workspace/uploads"
OUTPUT_DIR = "/workspace/outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upload_zip")
async def upload_zip(file: UploadFile = File(...)):
    session_id = str(uuid.uuid4())
    session_path = os.path.join(UPLOAD_DIR, session_id)
    os.makedirs(session_path, exist_ok=True)

    zip_path = os.path.join(session_path, file.filename)
    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image_folder = extract_zip(zip_path, session_path)
    model_path = generate_3d_model(image_folder, os.path.join(OUTPUT_DIR, session_id))

    return {"session_id": session_id, "output_model": model_path}

@app.get("/result/{session_id}")
def get_result(session_id: str):
    model_path = os.path.join(OUTPUT_DIR, session_id, "output.ply")
    if os.path.exists(model_path):
        return FileResponse(model_path, media_type="model/ply", filename="auto3d.ply")
    return {"error": "Model not found"}
