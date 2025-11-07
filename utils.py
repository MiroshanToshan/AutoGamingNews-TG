import requests

def download_picture(link_photo,path,headers):
    response = requests.get(link_photo,verify=False, headers=headers)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)

def generate_post_text(header, description, news_link):
    text = f'''
{header}

{description}

Ссылка на источник: {news_link}

'''
    return text
