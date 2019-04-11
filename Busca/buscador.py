import requests
import html5lib
from bs4 import BeautifulSoup 

# Baixando a página
def download(url):
	response = ''
	try:
		response = requests.get(url).text
	except requests.exceptions.RequestException as e:
		pass
	finally:
		return response

# Guardando trecho do texto contendo a palavra
def guadar_trecho(keyword, palavra, page):
	texto = ''
	tamanho_palavra = len(keyword)

	if palavra < 0:
		texto = 'Palavra não encontrada'
	elif palavra < 10:
		texto = page[0:palavra+10+tamanho_palavra:1]
	else:
		texto = page[palavra-10:palavra+10+tamanho_palavra:1]

	return texto

# Formatando os links 
def formatar_link(url):
	if url != None:
		if url.startswith('http://') or url.startswith('https://'):
			return url

# Mecanismo de busca
def busca(keyword, url, deth):

	# Atribuindo a página baixada em uma variavel
	pagina = download(url)

	# Criando um objeto BeautifulSoup
	pagina_soup = BeautifulSoup(pagina,'html.parser')
	page = pagina_soup.text

	# Buscando a palavra dentro da página
	palavra = page.find(keyword)

	# Saída
	print('Palavra --> %s' % keyword)
	print('Trecho  --> %s' % guadar_trecho(keyword,palavra,page))
	print('Origem  --> %s' % url)

	# Verificando a profundidade da busca 
	if deth > 0:

		# Criando um objeto BeautifulSoup
		html = BeautifulSoup(pagina,'html5lib')

		# Buscando os links dentro da página
		links = html.find_all('a')

		# Guardando os links em uma lista
		urls = []
		for link in links:
			urls.append(formatar_link(link.get('href')))


		# Fazendo a recursividade
		for url in urls:
			if url != None:
				busca(keyword, url, deth-1)
	
	
if __name__ == '__main__':
	busca('ifpi', 'http://www.ifpi.edu.br/', 1)