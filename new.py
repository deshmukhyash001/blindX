import os
from openai import OpenAI
from pathlib import Path
import base64

# Set your key (better to use .env file in real projects)
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),          # or just "your_key_here" if you hardcode (not recommended)
    base_url="https://api.x.ai/v1"
)

# Pick a vision-capable model (check docs/console for latest/best)
MODEL = "grok-4-0709"          # or "grok-2-vision-latest", "grok-vision-beta", etc.

# Example 1: Simple text-only chat
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant from xAI."},
        {"role": "user", "content": "Tell me a fun fact about Pune!"}
    ],
    temperature=0.7,
    max_tokens=300
)

print("Grok:", response.choices[0].message.content)

# Example 2: Send a picture + question (vision mode)
# Method A: Use public URL (easiest)
image_url = "https://example.com/your-photo.jpg"   # replace with real public image link

messages_with_image = [
    {"role": "user", "content": [
        {"type": "text", "text": "Describe this photo in detail and tell me what city it might be from?"},
        {"type": "image_url", "image_url": {"url": image_url}}
    ]}
]

response_image = client.chat.completions.create(
    model=MODEL,
    messages=messages_with_image,
    max_tokens=500
)

print("Grok about the image:", response_image.choices[0].message.content)

# Method B: Send local image file as base64 (no need for public URL)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

local_image_path = "path/to/your/photo.jpg"   # change this
base64_image = encode_image(local_image_path)

messages_local = [
    {"role": "user", "content": [
        {"type": "text", "text": "What's happening in this picture? Any funny details?"},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
    ]}
]

response_local = client.chat.completions.create(
    model=MODEL,
    messages=messages_local
)

print("Grok on local image:", response_local.choices[0].message.content)