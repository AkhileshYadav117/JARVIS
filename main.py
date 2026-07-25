import speech_recognition as sr  
import webbrowser 
import pyttsx3
import musicLibrary
import requests
from google import genai

#pip install pocketsphinx
recognizer=sr.Recognizer()
#engine=pyttsx3.init() 
newsapi="3e9907d2102e48ccb8d9b2a5e2ef5bcd"
# important command for my terminal if something went wrong is .\.venv\Scripts\python.exe
def speak(text):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') 
    
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = genai.Client(api_key="AQ.Ab8RN6LMNP_EU8rDEfTBDKFPOT5FfTj5nIdCHuT5t-oSENIPzw")
    prompt = f"Answer this short voice assistant command in one or two brief sentences: {command}"
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt, 
    )

    return response.text
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")	
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.be")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open gemini" in c.lower():
        webbrowser.open("https://gemini.com") 
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")  
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]  
        link = musicLibrary.music[song]
        webbrowser.open(link)     
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

        r = requests.get(url)
        data = r.json()
        
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            if not articles:
                speak("I found no articles for India right now.")
            else:
                speak("Here are the top headlines.")
                # Read out only the top 3 headlines so it doesn't loop infinitely
                for i, article in enumerate(articles[:5], start=1):
                    print(f"{i}. {article['title']}")
                    speak(f"Headline {i}: {article['title']}")
        else:
            # If the API throws an error, Jarvis will now explicitly tell you what went wrong!
            print("Error Message:", data.get("message"))
            speak(f"Sorry, the API returned an error: {data.get('message')}")
    else : # Let genAI handle the problem 
        output=aiprocess(c)
        speak(output)       
                             
if __name__ == "__main__":
    speak("Intializing Jarvis......")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone 
        r=sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio=r.listen(source,timeout=3,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Ya")
                #Listen for command 
                with sr.Microphone() as source:
                  print("Jarvis Active....")
                  audio = r.listen(source)  
                  command = r.recognize_google(audio)
             
                processCommand(command)      
                
        except Exception as e :
            print("Error;{0}".format(e))              
            
       
       
