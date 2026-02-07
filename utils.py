import ollama
import numpy as np
from PIL import Image
import base64
from io import BytesIO

def get_local_models():
    try:
        response = ollama.list()
        models = response.get("models", [])
        models_list = [model["model"] for model in models]
        return sorted(models_list) if models_list else ["No model detected"]
    except Exception:
        return ["No model detected"]

def tensor_to_base64_list(image_tensor):
    images_b64 = []
    if image_tensor is None:
        return images_b64

    for i in range(image_tensor.shape[0]):
        image = image_tensor[i].cpu().numpy()
        image = (image * 255).clip(0, 255).astype(np.uint8)

        # Forzar RGB para evitar problemas con canales Alpha
        pil = Image.fromarray(image).convert("RGB")
        buffer = BytesIO()
        pil.save(buffer, format="PNG")

        images_b64.append(base64.b64encode(buffer.getvalue()).decode("utf-8"))

    return images_b64