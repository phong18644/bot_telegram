import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1233893456:AAF7oo6oHOQ1I5pO9k8pcfLxRCjAZYulIB8'
    bot_chatID = '-1001460238485'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

