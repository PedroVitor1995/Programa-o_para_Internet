import requests
from lxml import html


def Questao01():
	response = requests.get('https://www.youtube.com')
	print("Status code: {}".format(response.status_code))
	print("Cabeçalhos: {}".format(response.headers))
	print("Tamanho da resposta: {}".format(len(response.content)))
	print("Corpo da resposta: {}".format(response.text))

def Questao02():
	url = 'http://libra.ifpi.edu.br/topo_ifpi.png'

	response = requests.get(url)

	with open('logo-ifpi.jpg','wb') as f:
		f.write(response.content)

def Questao03():
	url = 'https://www.suamusica.com.br'
	
	arquivo = open('links.txt', 'w')

	response = requests.get(url)
	pagina = html.fromstring(response.content)
	links = pagina.xpath('//a/@href')
	arquivo.write(str(links))

	arquivo.close()

if __name__ == '__main__':
	Questao01()
