import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_approval_notification(script_data):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    data = script_data.get("script", script_data)

    hook_object = data.get("hook", {})
    hook_text = hook_object.get("text", data.get("hook", "Hook not found.")) if isinstance(hook_object, dict) else str(hook_object)
    
    body_object = data.get("body", {})
    body_text = body_object.get("text", data.get("body", {}).get("text", "Body not found.")) if isinstance(body_object, dict) else str(body_object)

    cta_object = data.get("cta", {})
    cta_text = cta_object.get("text", data.get("cta", {}).get("text", "CTA not found.")) if isinstance(cta_object, dict) else str(cta_object)

    message = f"*New Viral Script Generated for Approval!*\n\n"
    message += f"*Hook:* {hook_text}\n"
    message += f"*Body:* {body_text}\n\n"
    message += f"*CTA:* {cta_text}\n\n"

    message += "Please approve with \"YES\" or reject with \"NO\"."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Approval notification sent successfully.")

if __name__ == "__main__":
    
    example_script = {
        "script": {
            "hook": {"text": "This is a viral hook!"},
            "description": {"text": "This is a description of the viral content."},
            "cta": {"text": "Click here to learn more!"}
        }
    }
    send_approval_notification(example_script)
