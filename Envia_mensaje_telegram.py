# Como enviar un mensaje a Telegram

import requests
TOKEN = "AQUI TU TOKEN"
chat_id = "TU CHAT ID"
message = "ESCRIBE AQUI TU MENSAJE 👍"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())