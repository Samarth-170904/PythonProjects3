import speech_recognition as sr
import webbrowser
import pyttsx3 as pyttsx
#import musiclib
#import requests as request # type: ignore



recognizer = sr.Recognizer()
engine = pyttsx.init()
#newsapi = "bb6c2974db1b46c6ab45cfc0e60d43fc"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def processcommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in c:  # Fixed typo
        webbrowser.open("https://www.linkedin.com/")
        speak("Opening LinkedIn")
    # elif c.lower().startswith("play"):
    #     song = c.lower().split(" ")[1]
    #     link = musiclib.music[song]
    #     webbrowser.open(link)
    #     speak(f"Playing {song}")
        
    # we can add open ai also but it is paid so i have not integrated 
        


if __name__ == '__main__':
    speak("Intializing luna...")
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Calibrate for 2 seconds
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                if text.lower() == "luna":
                    speak("Yes?")
                    print("luna active. Say a command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"{command}")
                    processcommand(command)
                    
            except sr.WaitTimeoutError:
                print("Timed out waiting for phrase. Still listening...")
            except sr.UnknownValueError:
                print("Couldn’t understand the audio.")
            except sr.RequestError as e:
                print(f"Google API error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        