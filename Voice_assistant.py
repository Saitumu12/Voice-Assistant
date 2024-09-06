import speech_recognition as sr
import pyttsx3
from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

while True:
    command = listen()
    if command:
        if "hello" in command.lower():
            speak("Hello! How can I assist you today?")
        elif "stop" in command.lower():
            speak("Goodbye!")
            break
        elif "weather" in command.lower():
            speak("Sure, I can tell you the weather. But I need an internet connection to provide that information.")
        elif "time" in command.lower():
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(f"The current time is {current_time}.")
        elif "your name" in command.lower():
            speak("I am your voice assistant. How can I help you today?")
        else:
            speak("Sorry, I don't understand that command.")

