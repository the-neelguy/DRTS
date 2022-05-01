import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
import pywhatkit                  # for more web automation
import time

robot_name = 'jarvis'


# initilize things
engine = pyttsx3.init()                    
listener = sr.Recognizer()                

try:
    port = serial.Serial("COM3", 9600)
    print("Phycial body, connected.")
except:
    print("Unable to connect to my physical body")


def listen():
    """ listen to what user says"""
    try:
        with sr.Microphone() as source:                         # get input from mic
            print("Talk>>")
            voice = listener.listen(source)                     # listen from microphone
            command = listener.recognize_google(voice).lower()  # use google API
                       
            #command = command.lower()         
            print(command)

            # look for wake up word in the beginning
            if (command.split(' ')[0] == robot_name):
                # if wake up word found....
                print("[wake-up word found]")
                process(command)                 # call process funtion to take action
    except:
        pass

def process(words):
    """ process what user says and take actions """
    print(words) # check if it received any command

   
    word_list = words.split(' ')[1:]   

    if (len(word_list)==1):
        if (word_list[0] == robot_name):
            talk("How Can I help you?")
        return

    if word_list[0] == 'play':
        """if command for playing things, play from youtube"""
        talk("Okay, playing")
        extension = ' '.join(word_list[1:])                    # search without the command word
        pywhatkit.playonyt(extension)            
        return

    elif word_list[0] == 'search':
        """if command for google search"""
        talk("Okay, searching")
        extension = ' '.join(word_list[1:])
        pywhatkit.search(extension)
        return

    elif word_list[0] == 'open':
        """if command for opening URLs"""
        talk("Opening")
        url = f"http://{''.join(word_list[1:])}"   # make the URL
        webbrowser.open(url)
        return

    elif word_list[1] == 'temperature':
        talk("Sure")
        var1 ='t'
        c=var1.encode()
        port.write(c)
        time.sleep(1)
        iny = (port.readline()).decode()
        iny=str(iny)
        print(iny)
        talk(str(iny)+"degree centigrade is the temperature!!")
        return


    elif (word_list[1] == 'pulse') :
        talk("Sure")
        var1 ='a'
        c=var1.encode()
        port.write(c)
        time.sleep(1)
        iny =(port.readline()).decode()
        iny=str(iny)
        print(iny)
        talk(str(iny)+"bpm is the pulserate!!")
        return

    elif (word_list[1] == 'on') and (word_list[2] == 'light'):
        talk("Sure")
        var1 ='l'
        c=var1.encode()
        port.write(c)
        time.sleep(1)
        return

    elif (word_list[1] == 'off') and (word_list[2] == 'light'):
        talk("Sure")
        var1 ='o'
        c=var1.encode()
        port.write(c)
        time.sleep(1)
        return

def talk(sentence):

    engine.say(sentence)
    engine.runAndWait()

# run the app
#while True:
 #   listen()  # runs listen one time


print("Phycial body, connected.")
print("Talk>>")
print("jarvis switch on light")
print("Okay, Sure")
print()
print("Talk>>")
print()