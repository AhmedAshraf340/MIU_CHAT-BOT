import speech_recognition
import textblob
from textblob import TextBlob
import os
# Defeinations Of Object To Speak
recognizer = speech_recognition.Recognizer()
def takeCommand():
     # Def Of obcject to recognize the voice command ( Voice Input )
    r = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-US')
        #query = r.recognize_google(audio, language ='ar-EG')
        #text_blob_object_arabic = TextBlob(query)
        #print (text_blob_object_arabic.translate(to="en"))
        print(f"User said: {query}\n")
        
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        #speak("Can't Recognize please repeat")
        s="can't hear"
        return s
     
    return query
