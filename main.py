from bs4 import BeautifulSoup
from urllib import request


url = 'https://aditiyadwiramadani.github.io/'
get_url = request.urlopen(url=url)
scarp = get_url.read(7000).decode('utf-8')
sampo = BeautifulSoup(scarp, 'html.parser')

def parse_biasa():
		for i in sampo.find_all('a'):
		    print(i.string)

def parse_class_url():
		class_nav = sampo.find_all('a', class_='nav-link')
		for i in class_nav:
		     print(i.string)

def html_tag():
     asp = sampo.div
     coso = asp.div.h1.string
     print(coso)


print('parse Biasa')
parse_biasa()
print('\nParse class Url ')
parse_class_url()
print('\n \n ')
html_tag()