from win32com.client import Dispatch
import speech_recognition as sr
import pickle
import os

def ask_mic_mode():
    global mic_mode
    if os.path.exists("C:/ellis_cache/mic_mode.dat"):
        print("", end="")
    else:
        while 1 == 1:
            # To ask if Mic is installed!
            print("Do you have a working mic?")
            say("Do you have a working microphone?")
            raw_input = input("You: ")
            # Evaluate and then convert to boolean
            if "yes" in raw_input or "Y" in raw_input:
                mic_mode = True
                break
            elif "no" in raw_input or "N" in raw_input:
                mic_mode = False
                break
            else:
                say("Please enter a valid input. Try with yes or no.")
        pickle.dump(mic_mode, open("C:/ellis_cache/mic_mode.dat", "xb"))


def take_voice_input(sword="You"):
    with sr.Microphone() as source:
        tries = 5
        while 1 == 1:
            if tries <= 0:
                say("Please enter with your keyboard!")
                vinput = input(sword + ": ")
                break
            else:
                print("")
            print("Listening!")
            audio = r.listen(source)
            print(sword + ": ", end="")
            try:
                text = r.recognize_google(audio)
                vinput = str("{}".format(text))
                print(vinput)
                tries = 5
                break
            except:
                say("Sorry! I could not recognise your voice!! Please try again!")
                tries -= 1
    return vinput


def say(tspeak, kword="Ellis"):
    print(kword + ": " + tspeak)
    speak.Speak(tspeak)


speak = Dispatch("SAPI.SpVoice")
r = sr.Recognizer()

