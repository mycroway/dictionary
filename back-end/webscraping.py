import requests
from bs4 import BeautifulSoup

def get(word_input):
	url = 'https://delp.pt/'+word_input
	res = requests.get(url)
	
	site = BeautifulSoup(res.content, 'html.parser')
	
	word_shapes_raw = site.findAll('span', attrs={'class', 'varpb'})
	word_shapes = []
	for i, word in enumerate(word_shapes_raw):
		if i < 2:
			word_shapes.append(word.text)
		
	
	defs_list = site.findAll('span', attrs={'class', 'def'})
	defs = []
	for i, def_list in enumerate(defs_list):
		if i == 0:
			word_from = def_list.text
		else:
			defs.append(def_list.text)
		
		
	return_datas = {
		'word': word_shapes,
		'defs': defs,
		'latin': word_from
	}
	
	return return_datas
