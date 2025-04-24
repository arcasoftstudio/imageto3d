import os
import subprocess

def run_cmd(cmd, cwd=None, desc=""):
    print(f"\n🚀 {desc}...")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print("✔️ STDOUT:\n", result.stdout)
    print("⚠️ STDERR:\n", result.stderr)
    result.check_returncode()

def generate_3d_model(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    gsplat_dir = "/workspace/gsplat"
    scene_dir = os.path.join(output_dir, "scene")
    os.makedirs(scene_dir, exist_ok=True)

    # Copy immagini
    image_target = os.path.join(scene_dir, "images")
    os.makedirs(image_target, exist_ok=True)
    for f in os.listdir(input_dir):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            src = os.path.join(input_dir, f)
            dst = os.path.join(image_target, f)
            os.system(f"cp '{src}' '{dst}'")

    # 1. Convert
    run_cmd(
        f"python convert.py -s {scene_dir} --camera-model OPENCV --resize 1024 768",
        cwd=gsplat_dir,
        desc="Converti immagini"
    )

    # 2. Train
    run_cmd(
        f"python train.py -s {scene_dir} -m {scene_dir}/output",
        cwd=gsplat_dir,
        desc="Allena modello Gaussian Splatting"
    )

    # 3. Export
    run_cmd(
        f"python export_ply.py -m {scene_dir}/output -o {output_dir}/output.ply",
        cwd=gsplat_dir,
        desc="Esporta modello .ply"
    )

    return os.path.join(output_dir, "output.ply")
