import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen and recognize speech
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

# Main loop
while True:
    command = listen()
    if command:
        if "hello" in command.lower():
            speak("Hello! How can I assist you today?")
        elif "stop" in command.lower():
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand that command.")
