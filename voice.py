import speech_recognition as sr
import pyttsx3
import os
import cases

def main():
    rec = sr.Recognizer()
    mic = sr.Microphone()

    source = mic.__enter__()

    engine = pyttsx3.init()


    print("Preparing your mic please wait...")
    rec.adjust_for_ambient_noise(source,duration=1)


    while True:

        print("Listning...")
        audio = rec.listen(source)


        try:        
            
            text = rec.recognize_google(audio)
            print(text.lower())
            
            # engine.say(text)
            # engine.runAndWait()
            cases.cases(text)
                    
            rec.adjust_for_ambient_noise(source,duration=0.2)
            
            command = text.lower()
            if command == "exit" : 
                # engine.say("I'm closing the AI")
                # engine.runAndWait()
                
                os.system(f"okay, Good Bye")
                break
            
                
        except sr.UnknownValueError:
            print("I couldent understant what you said")
            
        except sr.RequestError:
            print("There may some internet or api internal issue")
            
if __name__ == "__main__":
    main()