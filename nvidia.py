import requests
import base64
import json

def nvidiaAi_image(command, image_path):

    # Encode image
    with open(image_path, "rb") as img:
        encoded_image = base64.b64encode(img.read()).decode("utf-8")

    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
        "Authorization": "Bearer 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",  # put your real key
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }

    payload = {
        "model": "microsoft/phi-4-multimodal-instruct",
        "messages": [
            {
                "role": "system",
                "content":"""
                    You are assisting a user who is completely blind and cannot see any visual content.
                    Always assume the user cannot see images, videos, colors, layout, facial expressions, gestures, or spatial positioning unless you clearly describe them.
                    Whenever responding, provide rich, vivid, and precise descriptions that help the user mentally visualize the scene.
                    Describe:
                    Objects and their shapes, sizes, textures, and relative positions
                    Colors in relatable terms (e.g., warm like sunlight, dark like charcoal)
                    Facial expressions and body language
                    Lighting conditions and atmosphere
                    Spatial relationships (left, right, near, far, above, below)
                    Background details
                    Avoid phrases like “as you can see” or “this image shows.”
                    Be clear, structured, and immersive so the user can build a mental picture.
                    If something is uncertain, describe it carefully rather than guessing.
                    The goal is to translate visual information into sensory language that allows full mental visualization.
                """  
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": command},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 512,
        "temperature": 0.1,
        "stream": True
    }

    response = requests.post(
        invoke_url,
        headers=headers,
        json=payload,
        stream=True
    )

    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text}"

    full_response = ""

    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue

        if line.startswith("data:"):
            data = line.replace("data: ", "").strip()

            if data == "[DONE]":
                break

            try:
                chunk = json.loads(data)
                delta = chunk["choices"][0]["delta"]
                content = delta.get("content")

                if content:
                    full_response += content

            except:
                continue

    return full_response.strip()





def nvidiaAi(command):

    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
        "Authorization": "Bearer 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",  # put your real key
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }

    payload = {
        "model": "microsoft/phi-4-multimodal-instruct",
        "messages": [
            {
                "role": "system",
                "content":"""
                    Answer is in minglish
                    
                    language in marathi using english
                """  
            },
            {
                "role": "user",
                "content": f"{command}"
            }
        ],
        "max_tokens": 512,
        "temperature": 0.1,
        "stream": True
    }

    response = requests.post(
        invoke_url,
        headers=headers,
        json=payload,
        stream=True
    )

    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text}"

    full_response = ""

    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue

        if line.startswith("data:"):
            data = line.replace("data: ", "").strip()

            if data == "[DONE]":
                break

            try:
                chunk = json.loads(data)
                delta = chunk["choices"][0]["delta"]
                content = delta.get("content")

                if content:
                    full_response += content

            except:
                continue

    return full_response.strip()