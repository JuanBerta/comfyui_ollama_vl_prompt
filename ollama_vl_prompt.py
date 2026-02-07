from .utils import tensor_to_base64_list, get_local_models
from ollama import chat
import os
import json

# Ruta para cargar presets desde el archivo externo que creamos anteriormente
RESOURCES_PATH = os.path.dirname(os.path.realpath(__file__))
PRESETS_FILE = os.path.join(RESOURCES_PATH, "presets.json")

def load_presets():
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    
    # Fallback con el nuevo preset incluido
    return {
        "Follow Prompt Only": "You are a helpful assistant. Follow the user's instructions strictly and provide a concise response.\n",
        "IMage Generation": "You are generating an image creation prompt.\nDescribe the image clearly, focusing on subject, clothing, colors, materials, lighting, and style.\nDo NOT mention cameras, photos, or photographers.\nOutput a single concise prompt.\n",
        "Caption (Neutral)": "Describe the image accurately and neutrally.\nDescribe the elements in the image.\nOutput a single concise prompt.\n"
    }

class OllamaVLPredictPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        presets = load_presets()
        return {
            "required": {
                "preset": (list(presets.keys()),),
                "user_hint": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "model": (get_local_models(),),
                "keep_alive": ("FLOAT", {"default": 5.0}),
                "combine_all_images": (["True", "False"], {"default": "False"}),
            },
            "optional": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
                "image3": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_prompt",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "run"
    CATEGORY = "prompt/ollama"

    def run(self, preset, user_hint, model, keep_alive, combine_all_images, image1=None, image2=None, image3=None):
        presets = load_presets()
        prompt_base = presets.get(preset, "")
        
        if user_hint.strip():
            prompt_base += "\nUser Instruction: " + user_hint.strip()

        images_b64 = []
        for img in [image1, image2, image3]:
            if img is not None:
                images_b64.extend(tensor_to_base64_list(img))

        results = []

        # Lógica si NO hay imágenes (Modo solo texto)
        if not images_b64:
            try:
                print("Running Ollama with text-only prompt...")
                response = chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt_base}],
                    keep_alive=keep_alive,
                )
                results.append(response.message.content.strip())
                print("Ollama response:", results[-1])
            except Exception as e:
                results.append(f"Ollama error: {str(e)}")
                print("Ollama error:", str(e))
            return (results,)

        # Lógica con imágenes (existente)
        if combine_all_images == "True":
            try:
                print("Running Ollama with combined images...")
                response = chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt_base, "images": images_b64}],
                    keep_alive=keep_alive,
                )
                results.append(response.message.content.replace("\n", ", ").strip())
                print("Ollama response:", results[-1])
            except Exception as e:
                results.append(f"Ollama error: {str(e)}")
                print("Ollama error:", str(e))
        else:
            for img_b64 in images_b64:
                try:
                    print("Running Ollama with single image...")
                    response = chat(
                        model=model,
                        messages=[{"role": "user", "content": prompt_base, "images": [img_b64]}],
                        keep_alive=keep_alive,
                    )
                    results.append(response.message.content.replace("\n", ", ").strip())
                    print("Ollama response:", results[-1])
                except Exception as e:
                    results.append(f"Ollama error: {str(e)}")
                    print("Ollama error:", str(e))

        return (results,)