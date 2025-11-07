import requests
from pathlib import Path
from bs4 import BeautifulSoup




# def download_picture(link_photo,path):
#     response = requests.get(link_photo)
#     response.raise_for_status()

#     with open(path, "wb") as file:
#         file.write(response.content)


# folder_path = "./photos"
# picture_name = "photo"
# number = 0


# path = Path(folder_path, f"{picture_name}{number+1}.png")


# URL = 'https://coop-land.ru/news/31776-mnogopolzovatelskiy-shuter-eve-vanguard-vyydet-v-rannem-dostupe-letom-2025-goda.html'
# response = requests.get(URL,verify=False)
# soup = BeautifulSoup(response.text, features="html.parser")
# kvota = soup.find('div', class_="quote")
# textalign = kvota.find('div')
# images = textalign.find_all('img')

# for image in images:

#     a = image['data-src']
#     photo_url = f'https://coop-land.ru{a}'
#     print(photo_url)
#     download_picture(photo_url,path)


URL = 'https://www.igromania.ru/news/'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6066.0 Safari/537.36'}

response = requests.get(URL,verify=False, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, features='html.parser')
header = soup.find('a', class_='ShelfCard_cardLink__mSxdR')
post_link = f'https://www.igromania.ru{header["href"]}'
post_header = header.text

news_page = requests.get(post_link, )
news_page.raise_for_status()
soup_new = BeautifulSoup(news_page.text, features='html.parser')
post_img = soup_new.find('img', class_='MaterialCommonImage_picture__Z_3EU' )
photo_link = post_img['src']

news_link = soup.find('a', class_="ShelfCard_cardLink__mSxdR")
news_linker = f"https://www.igromania.ru{news_link['href']}"

description = soup.find('div', class_='ShelfCard_cardDescription__Tnd7y').text

print(news_linker)
print(photo_link)
print(description)
print(post_header)



