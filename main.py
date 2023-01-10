import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pipwin
import pyaudio


#Comments
#For the robot to listen to our voice/speech pip install speechRecognition
#To speak out, or text to speech pip install pyttsx3
#For advance control on browser pip install pywhatkit
#To get wikipedia data pip install wikipedia
#To get funny jokes pip install pyjokes
#To get pipwin pip install pipwin
#To get audio pipwin install pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'linda' in command:
                command = command.replace('linda', '')
                print(command)
    except:
        pass
    return command


def run_linda():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')          
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')      
       elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
      elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')
    elif 'X' in command:
        talk('Y')               
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_linda()
