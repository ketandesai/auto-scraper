import requests

URL = "https://www.pohankalexuschantilly.com/search/new-lexus-es-300h-chantilly-va/?ct=60&cy=20153&md=1199&tp=new"

page = requests.get(URL)

print(page.text)