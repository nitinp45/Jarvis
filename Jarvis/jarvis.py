
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser

engine=pyttsx3.init('sapi5')  #take voices from this sapi5
voices=engine.getProperty('voices')
#print(voices[0].id) 
engine.setProperty('voice', voices[0].id)  #setting voices for my project

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
        
    speak("Hello I am jarvis sir.Please tell how can i help you")
    
def takeCommand():
    #It takes microphone input from the user and returns in string format
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")  
     
            
