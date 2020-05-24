print("Loading Ellis! Please Wait")
import voice
from voice import *
from Default_Inputs import default_inputs
speak = voice.speak
import pickle


def home():
    while 1 == 1:
        if mic_mode:
            input1s = take_input_mic()
        else:
            input1s = take_input_nomic()
        default_inputs(input1s)


def take_input_mic():
    # To take inputs repeatedly!
    input1 = take_voice_input()
    return input1


def take_input_nomic():
    # To take inputs repeatedly!
    while 1 < 2:
        input1s = input("You: ")
        return input1s
while True:
    if os.path.exists("C:/ellis_cache/mic_mode.dat"):
        mic_mode = pickle.load(open("C:/ellis_cache/mic_mode.dat", "rb"))
        break
    else:
        ask_mic_mode()
home()
