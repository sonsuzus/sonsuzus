import requests
from bs4 import BeautifulSoup

v_key = input('https://www.youtube.com/watch?v=')

url = 'https://www.youtube.com/watch?v={}'.format(v_key)

soup = BeautifulSoup(requests.get(url).text, 'lxml')

print(soup.select_one('meta[itemprop="interactionCount"][content]')['content'])