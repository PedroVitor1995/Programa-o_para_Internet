import requests
import requests_cache
from bs4 import BeautifulSoup 

requests_cache.install_cache() # Implementando cache
#requests_cache.clear() # Limpando cache

paginas = [] # guadar todas as paginas e o seu nivel
paginas_palavra = [] # guardar todas as paginas contendo a palavra

# Baixa a página
def download(url):
	response = ''
	try:
		response = requests.get(url)
	except Exception as ex:
		response = None
	finally:
		return response

# Busca e guarda trecho do texto contendo a palavra
def busca_guarda_palavra(keyword,pagina):
	texto = ''
	tamanho_keyword = len(keyword)

	soup = BeautifulSoup(pagina.text,'html.parser')
	page = soup.text

	# Busca palavra
	palavra = page.find(keyword)

	# Guarda palavra
	if palavra < 0:
		texto = None
	elif palavra < 10:
		texto = page[0:palavra+tamanho_keyword+10:1]
	elif palavra > 10:
		texto = page[palavra-10:palavra+tamanho_keyword+10:1]

	return texto

# Formata link
def formatar_link(url,url_original):
	if url != None:
		if url.startswith('http://') or url.startswith('https://'):
			return url
		elif url.startswith('/'):
			return url_original + url
		else:
			return url

# Percorre os links
def percorre_links(pagina,url,deth,keyword):
	urls = [] # guardar os links da pagina

	# Cria objeto 
	soup = BeautifulSoup(pagina.text,'html.parser')

	# Busca os links dentro da página
	links = soup.find_all('a')
	
	# Guada os links em uma lista
	for link in links:
		if formatar_link(link.get('href'),url) != None:
			if deth > 0:
				urls.append(formatar_link(link.get('href'),url))

				url = formatar_link(link.get('href'),url)			
				paginas.append({'Url':url,'Nivel':deth})

	return urls

def busca(keyword,url,deth):
	pagina = download(url)

	if pagina != None:

		if busca_guarda_palavra(keyword,pagina) != None:
			print('------------------------------------------------------')
			print('Link   --> %s' % url)
			print('Trecho --> %s' % busca_guarda_palavra(keyword,pagina))
			paginas_palavra.append(url)	
		else:
			print('------------------------------------------------------')
			print('Link   --> %s' % url)
			print('Palavra não encontrada')

		# Percorre os links e faz a recursividade
		if deth > 0 :
			urls = percorre_links(pagina,url,deth,keyword)

			for url in urls:
				try:
					busca(keyword,url,deth-1)
				except:
					continue	

	else:
		print('------------------------------------------------------')
		print('Erro na requsição da pagina')

# Mostra todas paginas que contem a palavra
def mostra_paginas(keyword):
	if len(paginas_palavra) > 0:
		print('------------------------------------------------------')
		print('Paginas encontradas contendo a palavra %s' % keyword)
		for pagina in paginas_palavra:
			print(pagina)

# Ranqueia as paginas em primarias e segindarias
def ranqueia_paginas(deth):	
	if len(paginas_palavra)  > 0:
		print('------------------------------------------------------')
		print('--------Paginas primarias--------')
		for link in paginas_palavra:
			for url in paginas:
				if link == url['Url'] and url['Nivel'] == deth:
					print(url['Url'])

		print('--------Paginas segundarias-------')
		for link in paginas_palavra:
			for url in paginas:
				if link == url['Url'] and url['Nivel'] < deth:
					print(url['Url'])
	
def main():
	keyword = 'Brasil'
	url = 'http://www.google.com.br'
	deth = 1
	busca(keyword,url,deth)
	mostra_paginas(keyword)
	ranqueia_paginas(deth)

if __name__ == '__main__':
	main()
	