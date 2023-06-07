import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.sondakika.com'

def main():
    req = requests.get(url)

    if req.status_code != 200:
        print('Connection Error!')
        quit(1)

    page = req.content
    soup = BeautifulSoup(page, 'html.parser')

    links = list()

    slider = soup.find('div', attrs={'class': 'bx-pager'})
    for i, link in enumerate(slider.find_all('a', attrs={'class': ''})):
        print(i + 1, '-', link['title'], '-', 'https://www.sondakika.com' + link['href'])
        print()
        links.append(url + link['href'])

    while True:
        try:
            inp = int(input('Hangi haberi açmak istiyorsunuz? (Kapatmak için -1 girin): '))
            print(inp)
            if inp == -1:
                return
        except KeyboardInterrupt:
            print()
            return
        except:
            print('Lütfen geçerli bir değer giriniz!')
        else:
            if not (inp >= 1 and inp <= len(links)):
                print('Lütfen geçerli bir değer giriniz!')
            else:
                webbrowser.open(links[inp - 1], new=2, autoraise=True)

if __name__ == '__main__':
    main()
