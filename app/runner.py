import os
import subprocess

def generate_3d_model(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_model = os.path.join(output_dir, "output.ply")

    # Simulazione comando (sostituibile con real Gaussian Splatting/NeRF)
    subprocess.run([
        "echo", f"Simulated model generation from {input_dir} to {output_model}"
    ], check=True)

    # Simula creazione modello
    with open(output_model, "w") as f:
        f.write("ply\nformat ascii 1.0\ncomment Simulated model\n")

    return output_model
