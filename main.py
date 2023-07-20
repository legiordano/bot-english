import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, how can I help you?")

user_input = input(">> ")
speak(f"You said: {user_input}")

speak("Nice talking to you!") 