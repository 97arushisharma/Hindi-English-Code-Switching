from tkinter import *
#import speech_recognition as sr
import os, csv
import detectlanguage
from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
import difflib
import nltk

detectlanguage.configuration.api_key = "4a757fef0e4e952fd4296813c7f581ee"
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('corpus')

'''
def speak_():
	r = sr.Recognizer()                                                                                   
	with sr.Microphone() as source:
		print("Speak:")
		audio = r.listen(source) 
	a1=r.recognize_google(audio); 
'''

def gui():

	test = e1.get()
	testy = word_tokenize(test)

	sent = []
	lan = []
	hin = []

	translator = Translator()

	with open('normalisation_dataset.csv', 'r') as file:

		reader = csv.reader(file, delimiter='	')

		for row in reader:
			sent.append(row[0])   # stores the first column of all the rows
			lan.append(row[1])    # stores the 2nd column of all the rows
			hin.append(row[2])    # storesthe 3rd column of all the rows

	result= ''
	con_hin = ''

	for words in testy:
		maxi=0.90
		match=''  

		for i in range (0, 15966):
			if(difflib.SequenceMatcher(None, sent[i], words.lower()).ratio() > maxi):  # so that we get the word having highest ratio
				maxi=difflib.SequenceMatcher(None, sent[i], words.lower()).ratio() 
				if lan[i] == 'hi':
					match = hin[i]

		# if the typed word is not present in dataset then the typed word is sent as output
		if(match == ''):
			try:
				if(detectlanguage.simple_detect(words) != 'en'):
					match=words

				else:	
					x = translator.translate(words, dest='hi')
					match = x.text
				
			except Exception as e:
				print("Error with word " + words + ": " + str(e))
				match = words

		result = result + match + " "

	print(result)

	# code for translating the language
	# for extracting only converted text and omitting the other output parameters
	x = translator.translate(result, dest='en')
	y =  x.text
	print(y)
	text1.insert(INSERT, y+"\n")  # for displaying the result in the text box in GUI
	print()

	#POS tagging
	output_file=open('Hindi_POS/hindi.input.txt', 'w')
	output_file.write(result)
	output_file.close()	

	os.chdir('Hindi_POS')
	os.system('make tag')


# code for GUI

master = Tk()

Label(master, text="Your search",font=("Helvetica", 16), fg="red", bg="#ffffff", padx=100, pady=40).grid(row=3, column=1, sticky=W)

e1 = Entry(master)
e1.grid(row=3, column=1, padx=300, pady=40)

Button(master, text='Convert', command=gui, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4).grid(row=15, column=1, pady=10)
#Button(master, text='Speak', command=speak_, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4).grid(row=15, column=2, pady=10,sticky=W)

text1 = Text(master,height=10, bg="white", fg="#3498db",font=("Helvetica", 10))
text1.grid(row = 18,column=1, pady=100)
text1.insert(INSERT, "                                                                Result\n\n")
master.configure(background='#ffffff') 

mainloop( )
