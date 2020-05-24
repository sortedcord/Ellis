from voice import *
import requests

def get_temp_info(cite):
    # The whole thing is in try if the city is invalid it will turn to the default city
    try:
        # When the city name is included in the input!!
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + cite
        json_data = requests.get(url).json()

        # Temperature information
        # IN the following line the value is subtracted from 273 to show in celsius. K-273 = C
        current_temp = int(json_data['main']["temp"]) - 273
        current_min_temp = int(json_data['main']["temp_min"]) - 273
        current_max_temp = int(json_data['main']["temp_max"]) - 273

        # Display the whole information
        print("Temperatures: " + str(current_temp) + "    " + str(current_min_temp) + "(min)     " + str(current_max_temp) + "(max)")
        speak.Speak("The temperature in " + cite + "is " + str(current_temp) + " degrees celsius")

    except Exception as cite:
        print("Invalid city")
        say("Invalid city. The city is now New Delhi!")
        cite = "New Delhi"  # The default city can be changed!!
        get_temp_info(cite)


def get_air_pressure_info(cite):
    # The whole thing is in try if the city is invalid it will turn to the default city
    try:
        # When the city name is included in the input!!
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + cite
        json_data = requests.get(url).json()

        # Air Pressure
        current_air_pressure = str(json_data['main']["pressure"])

        # Display the whole information
        print("Air Pressure: " + current_air_pressure)
        speak.Speak("In" + cite + " the air pressure is " + current_air_pressure + " P.A")
    except Exception as cite:
        print("Invalid city")
        say("Invalid city. The city is now New Delhi!")
        cite = "New Delhi"  # The default city can be changed!!
        get_air_pressure_info(cite)


def get_humidity(citi):
    # The whole thing is in try if the city is invalid it will turn to the default city
    try:
        # When the city name is included in the input!!
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + citi
        json_data = requests.get(url).json()

        # Humidity
        current_humidity = str(json_data['main']["humidity"])

        # Display the whole information
        print("Humidity: " + current_humidity)
        speak.Speak("It is " + current_humidity + " percent humid.")

    except Exception as citi:
        print("Invalid city")
        say("Invalid city. The city is now New Delhi!")
        citi = "New Delhi"  # The default city can be changed!!
        get_weather_city(citi)


def get_weather_city(citi):
    # The whole thing is in try if the city is invalid it will turn to the default city
    try:
        # When the city name is included in the input!!
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + citi
        json_data = requests.get(url).json()

        # Overview of the weather
        weather_description = json_data['weather'][0]["description"]
        print("Ellis: Weather in " + citi + ": ")
        print("Currently: " + weather_description)

        # Temperature information
        get_temp_info(citi)

        # Air Pressure
        get_air_pressure_info(citi)

        # Humidity
        get_humidity(citi)
    except Exception as citi:
        print("Invalid city")
        say("Invalid city. The city is now New Delhi!")
        citi = "New Delhi"  # The default city can be changed!!
        get_weather_city(citi)


def get_weather():
    # The default city can be modified
    city = "New Delhi"
    say("You can change the default city in the settings!")

        # The whole thing is in try if the city is invalid it will turn to the default city
    try:
        # When the city name is included in the input!!
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + city
        json_data = requests.get(url).json()

        # Overview of the weather
        weather_description = json_data['weather'][0]["description"]

        # Temperature information
        # IN the following line the value is subtracted from 273 to show in celsius. K-273 = C
        current_temp = int(json_data['main']["temp"]) - 273
        current_min_temp = int(json_data['main']["temp_min"]) - 273
        current_max_temp = int(json_data['main']["temp_max"]) - 273

        # Air Pressure
        current_air_pressure = str(json_data['main']["pressure"])

        # Humidity
        current_humidity = str(json_data['main']["humidity"])

        # Display the whole information
        print("Ellis: Weather in " + city + ": ")
        print("Currently: " + weather_description)
        print("Temperatures: " + str(current_temp) + "    " + str(current_min_temp) + "(min)     " + str(
            current_max_temp) + "(max)")
        print("Air Pressure: " + current_air_pressure)
        print("Humidity: " + current_humidity)
        speak.Speak("In " + city + " it is currently " + weather_description)
        speak.Speak("The temp there is " + str(current_temp) + " with a minimum of " + str(current_min_temp))
        speak.Speak(" and a maximum of " + str(current_max_temp))
        speak.Speak("The air pressure is " + current_air_pressure + " P.A")
        speak.Speak("and it is " + current_humidity + " percent humid.")

    except Exception as citi:

        # The exception error is unecessory
        say("Invalid city. The city is now New Delhi!")
        citi = "New Delhi"  # The default city can be changed!!
        get_weather_city(citi)
