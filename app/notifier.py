import requests

BOT_TOKEN = "8136649503:AAFAg1QMGZxFDshX7TkcPDorP2PPSeUUsJE"
CHAT_ID = "5590661870"

def send_message(job):
    msg = f"""🚀 New Job!

{job['title']}
{job['link']}
"""

    url = f"https://api.telegram.org/YOUR BOT TOKEN/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })
