import torch
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import (
    create_pan_cameras,
    decode_latent_images,
    decode_latent_mesh,
)

import warnings

# Suppress FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Device setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
if torch.cuda.is_available():
    print(f"Running on GPU: {torch.cuda.get_device_name(0)}")
else:
    print("Running on CPU (this will be slower)")

# Load models and diffusion configuration
print("Loading models...")
xm = load_model('transmitter', device=device)
model = load_model('text300M', device=device)
diffusion = diffusion_from_config(load_config('diffusion'))
print("Models loaded successfully.")

# Parameters for latent sampling
batch_size = 5  # Reduce batch size for testing
guidance_scale = 20.0
prompt = "diamond lattice structure"  # Replace this prompt with your custom description

# Generate latents using the text prompt
print(f"Generating 3D object for prompt: '{prompt}'...")
latents = sample_latents(
    batch_size=batch_size,
    model=model,
    diffusion=diffusion,
    guidance_scale=guidance_scale,
    model_kwargs=dict(texts=[prompt] * batch_size),
    progress=True,
    clip_denoised=True,
    use_fp16=False,  # Disable mixed precision to ensure compatibility
    use_karras=True,
    karras_steps=32,  # Reduce steps for faster testing
    sigma_min=1e-3,
    sigma_max=160,
    s_churn=0,
)

print("Latent generation completed. Proceeding to rendering and saving.")

# Rendering parameters
render_mode = 'nerf'  # Options: 'nerf' or 'stf'
render_size = 64  # Rendering size (adjust for higher resolution)

# Create camera views for rendering
cameras = create_pan_cameras(render_size, device)
print(f"Rendering mode: {render_mode}")

# Process and save each latent
for i, latent in enumerate(latents):
    print(f"Processing latent {i + 1}/{len(latents)}...")

    # Decode images for rendering
    images = decode_latent_images(xm, latent, cameras, rendering_mode=render_mode)
    print(f"Rendered images for latent {i + 1}. Skipping GIF generation in non-notebook mode.")

    # Decode the latent into a mesh
    mesh = decode_latent_mesh(xm, latent).tri_mesh()

    # Save the mesh as .PLY and .OBJ files
    ply_filename = f"generated_mesh_{i}.ply"
    obj_filename = f"generated_mesh_{i}.obj"
    with open(ply_filename, 'wb') as ply_file:
        mesh.write_ply(ply_file)
    with open(obj_filename, 'w') as obj_file:
        mesh.write_obj(obj_file)

    print(f"Meshes saved: {ply_filename}, {obj_filename}")

print("All tasks completed successfully!")
