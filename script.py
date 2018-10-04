from bs4 import BeautifulSoup
from urllib.request import urlopen

web_link = 'https://www.dictionary.com/browse/'
word_list = open("input.txt","r")
sentence_list = open("output.txt", "w")
for line in word_list:
	try:
		page = urlopen(web_link + line.strip())
		soup = BeautifulSoup(page, 'html.parser')
		sentence_bx = soup.find(class_="css-1khtv86 e1rg2mtf2")
		sentence = sentence_bx.text.strip()
		sentence_list.write(line.strip() + " - " + sentence + " - ")
		sentence_bx = soup.find(class_="css-it69we e15kc6du7")
		sentence = sentence_bx.text.strip()
		sentence_list.write(sentence + "\n")
	except:
		print (line + " - word was not found\n")
sentence_list.close()