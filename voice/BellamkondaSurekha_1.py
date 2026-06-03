import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Text to Speech Engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
recognizer = sr.Recognizer()

def take_command():

    try:
        with sr.Microphone() as source:

            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print("You said:", command)

            return command

    except:
        return ""

# Welcome Message
speak("Hello! I am your voice assistant.")

while True:

    command = take_command()

    # Greeting
    if "hello" in command:
        speak("Hello, how are you?")

    # Time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)

    # Date
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    # Wikipedia Search
    elif "who is" in command:

        person = command.replace("who is", "")

        info = wikipedia.summary(person, 1)

        speak(info)

    # Open Google Search
    elif "search" in command:

        search_query = command.replace("search", "")

        speak("Searching on Google")

        pywhatkit.search(search_query)

    # Exit
    elif "exit" in command or "stop" in command:

        speak("Goodbye!")

        break

    # Unknown Command
    elif command != "":
        speak("Sorry, I did not understand.")