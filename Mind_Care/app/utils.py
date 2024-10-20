from together import Together
from flask import current_app

def get_ai_response(user_message, image_url=None):
    client = Together(base_url="https://api.aimlapi.com/v1", api_key=current_app.config['TOGETHER_API_KEY'])
    
    messages = [
        {
            "role": "system",
            "content": "You are a mental health care assistant. Provide structured and professional responses as a mental health doctor would."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_message,
                }
            ]
        }
    ]
    
    if image_url:
        messages[1]["content"].append({
            "type": "image_url",
            "image_url": {
                "url": image_url,
            }
        })

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        messages=messages,
        max_tokens=300,
    )
    
    return response.choices[0].message.content