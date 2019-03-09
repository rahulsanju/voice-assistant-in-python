from gtts import gTTS 
import speech_recognition as sr 
import os
import webbrowser
import smtplib


def talkToRahul(audio):
	print(audio)
	tts = gTTS(text=audio,lang='en')
	tts.save('audio.mp3')
	os.system('start audio.mp3')

def RahulsCommand():
	r = sr.Recognizer()
	print(r)
	with sr.Microphone() as source:
		print(sr.Microphone())
		print("Speak")
		r.pause_threshold=1
		r.adjust_for_ambient_noise(source,duration=1)
		audio = r.listen(source)
		print(audio)
		print("ads",str(audio))
	try :	
		command = r.recognize_google(audio)
		print('you said: '+command+'\n')

	except sr.UnknownValueError:
		assistant(RahulsCommand())

	return command

def assistant(command):
	if 'facebook' in command:
		url = 'https://www.facebook.com'
		webbrowser.open_new_tab(url)
		
	if 'youtube' in command:	
		url = 'https://www.youtube.com'
		webbrowser.open_new_tab(url)

	if 'github' in command:
		url = 'https://www.github.com'
		webbrowser.open_new_tab(url)

	if 'hello' in command:
		talkToRahul('how can i help you ?')
	

#talkToRahul('hello Rahul. How can i help you? I am Your Voice Assistant,Nami. I am opening Google for you')
#talkToRahul('Say Something')
#webbrowser.open_new_tab('http://www.google.com')
while True:
	assistant(RahulsCommand())
