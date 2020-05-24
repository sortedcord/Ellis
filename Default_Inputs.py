from joke_module import tell_joke
from Calculations import *
from Youtube import *
from space import space
from weather_api import *
from ask_wikipedia import do_wiki
from dtime import get_today_date
mic_mode = pickle.load(open("C:/ellis_cache/mic_mode.dat", "rb"))


def default_inputs(input1s):
    # If there is an input for hello!
    if input1s == "Hello" or input1s == "hello" or input1s == "hi" or input1s == "high":
        say("hi there")

    # If there is an input of why or y becouse they sound the same!!
    elif input1s == "why" or input1s == "y":
        say("Just like that")

    # IF the input contains what is the weather. It detects the city according to in.
    elif "what is the weather" in input1s or input1s == "what is the weather now" or input1s == "what is the weather outside":
        if "in" in input1s:
            w_info = input1s.split("in ")
            city = w_info[-1]
            get_weather_city(city)
        else:
            # Call the normal weather funtion!
            get_weather()
    elif input1s == "how are you" or input1s == "what's up" or input1s == "What is up":
        say("I am doing just fine and what about you?")
        if mic_mode:
            input1t = take_voice_input()
        else:
            input1t = input("You: ")

        if "fine" in input1t or "good" in input1t or "okay" in input1t:
            say("That's good to hear!")
        else:
            say("Hope a joke will make your day!")
            joke = tell_joke()
            say(joke)

    # If the person asks today's date!
    elif "what is the date" in input1s or "date" in input1s and "today" in input1s or "today's" in input1s:
        get_today_date()

    # Greetngs!
    elif "thank" in input1s or "thanks" in input1s:
        say("You're welcome!")

    # Just for fun
    elif "who is your father" == input1s:
        say("I am created by Aditya Gupta. Feels good to talk about my father!")

    elif "who is your mother" == input1s:
        say("I was made on Python 3.6.8 with APIs. Maybe it is my mother")

    elif "what is your fathers" in input1s or "what does your father" in input1s or "what is father's" in input1s or "what is your mothers" in input1s or "what does your mother" in input1s or "what is mother's" in input1s:
        say("Let's talk about me and not about my family. Okay!!")

    # Ask the terms! From wikipedia!
    elif "what is" in input1s:
        do_wiki(input1s, "is")
    elif "who is" in input1s:
        do_wiki(input1s, "is")
    elif "who was" in input1s:
        do_wiki(input1s, "was")
    elif "play" in input1s:
        sss = input1s.split("play ")
        song_desc = sss[-1]
        get_song(song_desc)
        title = get_titles()
        say("Alright! Playing " + title + " from youtube!")
        space(2)
        play_song(song_desc)

    # Calculations
    elif "add" in input1s and "and" in input1s:
        sum = add(input1s)
        say("The sum is " + str(sum))

    elif "plus" in input1s and "and" in input1s:
        sum = plus(input1s)
        say("The sum is " + str(sum))

    elif "sub" in input1s and "and" in input1s:
        difference = diffandsub(input1s)
        say("The difference is " + str(difference))

    elif "subtract" in input1s and "and" in input1s:
        difference = diffandsubtract(input1s)
        say("The difference is " + str(difference))

    elif "minus" in input1s and "and" in input1s:
        difference = diffandminus(input1s)
        say("The difference is " + str(difference))

    elif "sub" in input1s and "from" in input1s:
        difference = diffFromsub(input1s)
        say("The difference is " + str(difference))

    elif "subtract" in input1s and "from" in input1s:
        difference = diffFromsubtract(input1s)
        say("The difference is " + str(difference))

    elif "minus" in input1s and "from" in input1s:
        difference = diffFromminus(input1s)
        say("The difference is " + str(difference))

    else:
        say("I don't understand!")

