import os
import json
from .utils import tensor_to_base64_list, get_local_models
from ollama import chat

# Get the route of the JSON file in the same folder than the script
RESOURCES_PATH = os.path.dirname(os.path.realpath(__file__))
PRESETS_FILE = os.path.join(RESOURCES_PATH, "presets.json")

def load_presets():
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading presets.json: {e}")
    # Fallback in case that the file doesn't exists or is corrupt
    return {"Default": "Describe this image."}

class OllamaVLPredictPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        # We load the presets here so they are updated when Comfyui is updated
        presets = load_presets()
        return {
            "required": {
                "image1": ("IMAGE",),
                "preset": (list(presets.keys()),), # Dynamic from the JSOn
                "user_hint": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "model": (get_local_models(),), #
                "keep_alive": ("FLOAT", {"default": 5.0}),
                "combine_all_images": (["True", "False"], {"default": "False"}),
            },
            "optional": {
                "image2": ("IMAGE",),
                "image3": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_prompt",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "run"
    CATEGORY = "prompt/ollama" # 

    def run(self, image1, preset, user_hint, model, keep_alive, combine_all_images, image2=None, image3=None):
        # Reload the prests for obtain the text from the selected
        presets = load_presets()
        prompt_base = presets.get(preset, "Describe this image.")

        images_b64 = []
        for img in [image1, image2, image3]:
            if img is not None:
                images_b64.extend(tensor_to_base64_list(img)) #

        if user_hint.strip():
            prompt_base += "\nAdditional instruction: " + user_hint.strip()

        results = []
        
        # Delivery logic (Combined or Individual)
        if combine_all_images == "True":
            try:
                response = chat(
                    model=model,
                    messages=[{"role": "user", "content": prompt_base, "images": images_b64}],
                    keep_alive=keep_alive,
                )
                results.append(response.message.content.replace("\n", ", ").strip())
            except Exception as e:
                results.append(f"Ollama error: {str(e)}")
        else:
            for img_b64 in images_b64:
                try:
                    response = chat(
                        model=model,
                        messages=[{"role": "user", "content": prompt_base, "images": [img_b64]}],
                        keep_alive=keep_alive,
                    )
                    results.append(response.message.content.replace("\n", ", ").strip())
                except Exception as e:
                    results.append(f"Ollama error: {str(e)}")

        return (results,)