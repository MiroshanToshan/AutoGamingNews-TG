import json

import requests
from pprint import pprint



def send_message(token, chat_id, message):   

    params = {
        'chat_id' : chat_id,
        'text': message,
        'parse_mode' : 'Markdown'

    }

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    response = requests.get(url , params=params)
    response.raise_for_status()



def send_pictures(token,chat_id,text,path_to_files):

    media = [
    ]

    for number,file_path in enumerate(path_to_files):
        media_dict = {
            "type": "photo",
            "media": f"attach://random-name-{number+1}"
        }
        media.append(media_dict)



    media[0] ["caption"] = text

    params = {
          
        "chat_id": chat_id,
        "media": json.dumps(media),
        "contentType": "application/json"
    }


    files = {}

    for number, file_path in enumerate(path_to_files):

       files[f"random-name-{number+1}"] = open(f"{file_path}", "rb")


    send_text = f'https://api.telegram.org/bot{token}/sendMediaGroup'

    response = requests.get(send_text, params=params, files=files)
    response.raise_for_status()
