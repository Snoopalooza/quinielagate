from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from random import randint

currentLeague = 1928
lastLeague = 2018
fileJornadas = open("jornadasLiga.csv", "a+")
fileEquipos = open("equiposLiga.csv", "a+")
while currentLeague <= lastLeague:
	if (currentLeague not in [1936, 1937, 1938]):
		# add one to the last two digits, keep only the last two digits of that
		league = f't{str(currentLeague)}-{str(int(str(currentLeague)[2:])+1)[-2:]}'
		print('getting data from '+str(league))
		response = urlopen(f'https://www.bdfutbol.com/es/t/{league}.html')
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		js = str(soup.find(id="resultats"))
		start = js.find('SE=[];')
		separator = js.find('SP=new Array();')
		end = js.rfind(';')
		print('js')
		print(start)
		print(separator)
		print(end)
		fileEquipos.write(js[start:separator])
		fileJornadas.write(js[separator:end+1])
		print('file updated')
		time.sleep(1+randint(0,5))
	currentLeague += 1
	print('next league is '+str(currentLeague))

fileJornadas.close()
fileEquipos.close()
