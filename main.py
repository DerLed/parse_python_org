import requests as requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get('https://www.python.org')
    with open('test.html', 'w', encoding="utf-8") as file:
        file.write(response.text)
    with open("test.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        print(soup.find("div", attrs={"class": "medium-widget event-widget last"}))

