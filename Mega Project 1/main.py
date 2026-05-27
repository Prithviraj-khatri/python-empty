import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    pass

if __name__ == "__main__":
    speak("initializing jarvis")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from microphone
        r = sr.Recognizer()
       

        # recognize specc using sphinx_audio
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                print("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("listening....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("error ;{0}".format(e))
    
