from bs4 import BeautifulSoup
from urllib.request import urlopen

def fix_pron(str):
	fixed_str = ""
	start = False
	for letter in str:
		if(letter == ']'):
			fixed_str += ']'
			break
		else:
			if(start):
				fixed_str +=  letter
			if(letter == '['):
				start = True
				fixed_str += '['
	return fixed_str

web_link = 'https://www.dictionary.com/browse/'
word_list = open("input.txt","r")
sentence_list = open("output.txt", "w")
notfound_list = open("notfound.txt", "w")
for line in word_list:
	try:
		page = urlopen(web_link + line.strip())
		soup = BeautifulSoup(page, 'html.parser')
		sentence_bx = soup.find(class_="css-1khtv86 e1rg2mtf2")
		sentence = str(sentence_bx.text.encode('ascii','ignore'))
		sentence = fix_pron(sentence)
		sentence_list.write(line.strip() + " - " + sentence.strip() + " - ")
		sentence_bx = soup.find(class_="css-it69we e15kc6du7")
		sentence = sentence_bx.text.strip()
		sentence_list.write(sentence + "\n")
		print(line.strip() + " - Found!")
	except:
		print(line.strip() + " - Not Found!")
		notfound_list.write(line)
sentence_list.close()
notfound_list.close()