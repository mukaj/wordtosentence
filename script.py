from bs4 import BeautifulSoup
import urllib2

web_link = 'https://www.merriam-webster.com/dictionary/'
word_list = open("input.txt","r")
sentence_list = open("output.txt", "w")
for line in word_list:
	try:
		page = urllib2.urlopen(web_link + line.strip())
		soup = BeautifulSoup(page, 'html.parser')
		sentence_bx = soup.find(class_="definition-inner-item")
		sentence = sentence_bx.text.strip()
		sentence_list.write(sentence + "\n")
	except:
		print line + " - word was not found\n"