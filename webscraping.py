import requests
from bs4 import BeautifulSoup

def get_word(word):
	url = 'https://delp.pt/'+word
	res = requests.get(url)
	content = res.content
	
	site = BeautifulSoup(content, 'html.parser')
	
	word_res = site.find('span', attrs={'class', 'varpb'}).text
	
	return word_res