import ollama
import numpy as np
from PIL import Image
import base64
from io import BytesIO

def get_local_models():
    try:
        response = ollama.list()

        models = response.get("models", [])
        models_list = []
        for model in models:
            models_list.append(model["model"])

        return sorted(models_list) if models_list else ["No model detected, ensure Ollama is Active"]

    except Exception:
        # Never crash ComfyUI
        return ["No model Detected, ensure Ollama is Active"]

def tensor_to_base64_list(image_tensor):
    """
    Converts a batched ComfyUI IMAGE tensor into a list of base64 PNG images.
    """
    images_b64 = []

    for i in range(image_tensor.shape[0]):
        image = image_tensor[i]
        image = image.cpu().numpy()
        image = (image * 255).clip(0, 255).astype(np.uint8)

        pil = Image.fromarray(image)
        buffer = BytesIO()
        pil.save(buffer, format="PNG")

        images_b64.append(
            base64.b64encode(buffer.getvalue()).decode("utf-8")
        )

    return images_b64