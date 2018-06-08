from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import speech_recognition as sr

import pyttsx3
import pyaudio

bot = ChatBot('Jarvis')
speak = pyttsx3.init('sapi5')

def Speak(text):
    speak.say(text)
    speak.runAndWait()

chats = ["hi", "hello", "I'm fine", "thanks", "I'm Jarvis", "the future"]

bot.set_trainer(ListTrainer)
bot.train(chats)

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        try:
            print("Diga alguma coisa...")
            audio = r.listen(s)

            speech = r.recognize_google(audio)
            response = bot.get_response(speech)
            print('You: ',speech)
            print('Bot: ', response)
            Speak(response)
        except:
            print("Não entendi...")

        print(bot.get_response(speech))
