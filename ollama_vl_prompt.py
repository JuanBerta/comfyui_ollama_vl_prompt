from .utils import tensor_to_base64_list, get_local_models
from ollama import chat

PRESETS = {
    "SDXL": (
        """You are generating a Stable Diffusion XL image creation prompt.\n
        Describe the image clearly, focusing on subject, clothing, colors.\n
        materials, lighting, and style.\n
        Do NOT mention cameras, photos, or photographers.\n
        Output a single concise prompt.\n
        If multiple images are provided, treat them as contextual references.\n"""
    ),

    "Inpainting (Preserve Context)": (
        """Describe the image for Stable Diffusion inpainting.\n
        Focus on what should remain unchanged and the surrounding context.\n
        Avoid global changes unless necessary.\n
        If multiple images are provided, treat them as contextual references.\n"""
    ),

    "Anime / Illustration": (
        """Describe the image as an anime-style illustration prompt.\n
        Include art style, line quality, color palette, and mood.\n
        Do not mention real-world photography terms.\n
        Output a single concise prompt.\n
        If multiple images are provided, treat them as contextual references.\n"""
    ),

    "Caption (Neutral)": (
        """Describe the image accurately and neutrally.\n
        Describe the elements in the image.\n
        Output a single concise prompt.\n
        If multiple images are provided, treat them as contextual references.\n"""
    ),

    "Qwen Image Edit 2511": (
        """You are generating a Qwen Image Edit 2511 image editing prompt.\n
        Describe the image clearly, focusing on subject, clothing, colors\n
        materials, lighting, and style.\n
        Do NOT mention cameras, photos, or photographers.\n
        Output a single concise prompt.\n
        Example prompt: Change her hair to white.\n
        "If multiple images are provided, treat them as contextual references.\n"""
        
    ),

    "NSFW": (
        """You are generating NSFW Image prompt.\n
        Based on the image, utilize the elements present to generate a prompt.\n
        Take in account materials, lighting, and style.\n
        Do NOT mention cameras, photos, or photographers.\n
        Output a single concise prompt.\n
        If multiple images are provided, treat them as contextual references.\n"""
    ),

    "SFW": (
        """You are generating SFW Image prompt.\n
        In no case write NSFW/Questionable/Explicit elements in the prompt.\n
        Based on the image, utilize the elements present to generate a prompt.\n
        Take in account materials, lighting, and style.\n
        Do NOT mention cameras, photos, or photographers.\n 
        Output a single concise prompt.\n"""
    ),
}

class OllamaVLPredictPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image1": ("IMAGE",),
                "preset": (list(PRESETS.keys()),),
                "user_hint": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "model": (get_local_models(),),
                "keep_alive": ("FLOAT",),
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
    CATEGORY = "prompt/ollama"

    def run(
    self,
    image1,
    preset,
    user_hint,
    model,
    keep_alive,
    image2=None,
    image3=None,
    ):
        images_b64 = []

        if image1 is not None:
            images_b64.extend(tensor_to_base64_list(image1))

        if image2 is not None:
            images_b64.extend(tensor_to_base64_list(image2))

        if image3 is not None:
            images_b64.extend(tensor_to_base64_list(image3))

        prompt_base = PRESETS[preset]
        if user_hint.strip():
            prompt_base += "\nAdditional instruction: " + user_hint.strip()

        results = []

        for img_b64 in images_b64:
            try:
                response = chat(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt_base,
                            "images": [img_b64],
                        }
                    ],
                    keep_alive=keep_alive,
                )
                text = response.message.content
            except Exception as e:
                text = f"Ollama error: {str(e)}"

            results.append(text.replace("\n", ", ").strip())

        return (results,)
