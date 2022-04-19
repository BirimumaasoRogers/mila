# Import Libraries
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

from oculus import speak
# import pyaudio



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty
engine.setProperty('voice', voices[25].id)
engine.setProperty('rate', 50)
print(voices[25].id)
engine.say("I am the new sound, tell me anything you need me to do and i will do for you")
engine.runAndWait()
engine.stop()



# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>= 0 and hour<12:
#         speak("Good Morning Sir !")
  
#     elif hour>= 12 and hour<18:
#         speak("Good Afternoon Sir !")  
  
#     else:
#         speak("Good Evening Sir !") 
  
#     assname =("Oculus 1 point 0")
#     speak("I am your Assistant")

# def take_command():

#     with sr.Microphone() as source:
#         print("Listening...")
#         voice = listener.listen(source)
#         command = listener.recognize_google(voice)
#         command = command.lower()
#         if 'mila' in command:
#             command = command.replace('mila', '')
#             print(command)
#     return command

# def run_mila():
#     command = take_command()
#     print(command)
#     if 'play' in command:
#         song = command.replace('play', '')
#         speak('Playing ', + song)
#         pywhatkit.playonyt(song)

#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         speak('Current time is ', + time)

#     elif 'info' in command:
#         person = command.replace('info', '')
#         info = wikipedia.summary(person, 1)
#         speak(info)

#     elif 'how are you' in command:
#         speak('I am fine, how are you?')
    
#     elif 'mila' in command:
#         wishMe()
#         speak('Mila is here to assist you Rogers')

#     elif 'I am fine' in command:
#         speak('That is great, how may i help you today?')

#     elif 'joke' in command:
#         speak(pyjokes.get_joke())
        
#     else:
#         speak('I didnt quite get you')
#         speak('Please say that again')

# while True:
#     run_mila()