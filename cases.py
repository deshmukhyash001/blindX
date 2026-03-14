from email.mime import image
import os
import webbrowser
import datetime
import random
import string
from OpenAi import AiAsistant
from groke import grokeAi
from nvidia import nvidiaAi, nvidiaAi_image

import cv2

from groke import grokeAi

import cv2
import time

# def click_photo():
#     cam = cv2.VideoCapture(0)

#     if not cam.isOpened():
#         return False

#     # Warm up the camera (very important)
#     time.sleep(1)  # wait 1 second

#     # Throw away first few frames
#     for _ in range(10):
#         cam.read()

#     ret, frame = cam.read()

#     if ret:
#         cv2.imwrite("new_image.jpeg", frame)
#         cam.release()
#         return "new_image.jpeg"
#     else:
#         cam.release()
#         return False
        
#     cam.release()
#     cv2.destroyAllWindows


def cases(command):
    command = command.lower().strip()

    # =============================
    # 0 Image Capturing
    # =============================

    # =============================
    # 1–10 TIME & DATE
    # =============================

    # if "time" in command:
    #     now = datetime.datetime.now().strftime('%I:%M %p')
    #     return(f"The current time is {now}")
    

    if "date" in command:
        today = datetime.datetime.now().strftime('%A, %d %B %Y')
        return(f"Today is {today}")

    elif "day today" in command:
        return(datetime.datetime.now().strftime('%A'))

    elif "month" in command:
        return(datetime.datetime.now().strftime('%B'))

    elif "year" in command:
        return(datetime.datetime.now().strftime('%Y'))

    elif "good morning" in command:
        return("Good morning. I hope you have a wonderful day.")

    elif "good night" in command:
        return("Good night. Rest well.")

    elif "good evening" in command:
        return("Good evening.")

    elif "how are you" in command:
        return("I am functioning perfectly and ready to assist you.")

    elif "who are you" in command:
        return("I am your voice assistant designed for accessibility.")

    # =============================
    # 11–30 WEB COMMANDS
    # =============================

    elif "open google" in command:
        return("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        return("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif "open github" in command:
        return("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "open gmail" in command:
        return("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif "open drive" in command:
        return("Opening Google Drive.")
        webbrowser.open("https://drive.google.com")

    elif "open maps" in command:
        return("Opening Google Maps.")
        webbrowser.open("https://maps.google.com")

    elif "open news" in command:
        return("Opening news page.")
        webbrowser.open("https://news.google.com")

    elif "check weather" in command:
        return("Opening weather page.")
        webbrowser.open("https://google.com/search?q=weather")

    elif "search google" in command:
        query = command.replace("search google", "").strip()
        if query:
            return(f"Searching Google for {query}")
            webbrowser.open(f"https://google.com/search?q={query}")
        else:
            return("Please tell me what to search.")

    elif "search youtube" in command:
        query = command.replace("search youtube", "").strip()
        if query:
            return(f"Searching YouTube for {query}")
            webbrowser.open(f"https://youtube.com/results?search_query={query}")
        else:
            return("Please tell me what to search.")

    # =============================
    # 31–50 SYSTEM CONTROL
    # =============================

    elif "open terminal" in command:
        return("Opening terminal.")
        os.system("open -a Terminal")

    elif "open calculator" in command:
        return("Opening calculator.")
        os.system("open -a Calculator")

    elif "open calendar" in command:
        return("Opening calendar.")
        os.system("open -a Calendar")

    elif "open notes" in command:
        return("Opening notes.")
        os.system("open -a Notes")

    elif "open mail" in command:
        return("Opening mail.")
        os.system("open -a Mail")

    elif "open downloads" in command:
        return("Opening downloads folder.")
        os.system("open ~/Downloads")

    elif "open documents" in command:
        return("Opening documents folder.")
        os.system("open ~/Documents")

    elif "check battery" in command:
        return("Checking battery status.")
        os.system("pmset -g batt")

    elif "system uptime" in command:
        return("Checking system uptime.")
        os.system("uptime")

    elif "check disk space" in command:
        return("Checking disk space.")
        os.system("df -h")

    # =============================
    # 51–70 MUSIC & MEDIA
    # =============================

    elif "play music" in command:
        return("Opening music application.")
        os.system("open -a Music")

    elif "pause music" in command:
        return("Pausing music.")
        os.system("osascript -e 'tell application \"Music\" to pause'")

    elif "next song" in command:
        return("Playing next song.")
        os.system("osascript -e 'tell application \"Music\" to next track'")

    elif "previous song" in command:
        return("Playing previous song.")
        os.system("osascript -e 'tell application \"Music\" to previous track'")

    elif "stop music" in command:
        return("Stopping music.")
        os.system("osascript -e 'tell application \"Music\" to stop'")

    elif "volume up" in command:
        return("Increasing volume.")
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

    elif "volume down" in command:
        return("Decreasing volume.")
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")

    elif "mute system" in command:
        return("Muting system.")
        os.system("osascript -e 'set volume with output muted'")

    elif "unmute system" in command:
        return("Unmuting system.")
        os.system("osascript -e 'set volume without output muted'")

    elif "open camera" in command:
        return("Opening camera.")
        os.system("open -a Photo Booth")

    # =============================
    # 71–90 MEMORY & NOTES
    # =============================

    elif "remember this" in command:
        note = command.replace("remember this", "").strip()
        if note:
            with open("memory.txt", "a") as f:
                f.write(note + "\n")
            return("Your note has been saved.")
        else:
            return("Please tell me what to remember.")

    elif "show memory" in command:
        return("Reading your saved notes.")
        try:
            with open("memory.txt", "r") as f:
                notes = f.readlines()
                if notes:
                    for note in notes:
                        return(note.strip())
                else:
                    return("You have no saved notes.")
        except:
            return("Memory file not found.")

    elif "clear memory" in command:
        open("memory.txt", "w").close()
        return("All memory cleared.")

    # =============================
    # 91–120 FUN & INTERACTION
    # =============================

    elif "tell joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did Python go to school? To improve its class."
        ]
        return(random.choice(jokes))

    elif "flip a coin" in command:
        return(random.choice(["Heads", "Tails"]))

    elif "roll a dice" in command:
        return(f"You rolled {random.randint(1,6)}")

    elif "random number" in command:
        return(f"Your random number is {random.randint(1,100)}")

    elif "generate password" in command:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return(f"Your password is {password}")

    elif "motivate me" in command:
        return("Stay consistent. Discipline builds success.")

    elif "tell me a fact" in command:
        return("Honey never spoils.")

    elif "help" in command:
        return("You can ask about time, date, search web, play music, or save notes.")

    elif "repeat" in command:
        return("Please tell me what to repeat.")

    elif "guide me" in command:
        return("You can say commands like what is the time, open YouTube, tell joke, or remember this.")

    # =============================
    # 121–150 ADVANCED + SAFETY
    # =============================

    elif "slow mode" in command:
        return("Slow speech mode activated.")
        os.system("say -r 120 Slow mode activated")

    elif "fast mode" in command:
        return("Fast speech mode activated.")
        os.system("say -r 250 Fast mode activated")

    elif "what is artificial intelligence" in command:
        return("Artificial intelligence is simulation of human intelligence in machines.")

    elif "who is prime minister of india" in command:
        return("Narendra Modi is the Prime Minister of India.")

    elif "what is python" in command:
        return("Python is a powerful programming language.")

    elif "what is javascript" in command:
        return("JavaScript is the language of the web.")

    elif "are you intelligent" in command:
        return("I am continuously learning and improving.")

    elif "do you sleep" in command:
        return("I do not sleep. I am always ready.")

    elif "exit" in command or "stop listening" in command:
        return("Are you sure you want to exit? Say confirm to proceed.")

    elif "confirm" in command:
        return("Assistant shutting down. Goodbye.")
        exit()
        
    elif "around" in command:
        image = "new_image.jpeg"
        if image:
            data = nvidiaAi_image(command,image)
            return data
            
        else:
            return("Can't get your view")
        
    else:
        data = nvidiaAi(command)
        return(data)
