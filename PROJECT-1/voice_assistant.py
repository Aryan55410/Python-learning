import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import requests
import time
import webbrowser

# -------------------------
# CONFIGURATION
# -------------------------
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
reminders = []

# -------------------------
# TEXT-TO-SPEECH ENGINE
# -------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speed
engine.setProperty("volume", 1)  # Volume 0-1

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# -------------------------
# SPEECH RECOGNITION
# -------------------------
listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except:
        return ""

# -------------------------
# WEATHER FUNCTION
# -------------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "Sorry, I couldn't get the weather."

# -------------------------
# REMINDER FUNCTION
# -------------------------
def set_reminder(text, seconds):
    speak(f"Setting reminder: {text} in {seconds} seconds.")
    reminders.append((time.time() + seconds, text))

def check_reminders():
    current_time = time.time()
    for reminder in reminders[:]:
        if current_time >= reminder[0]:
            speak(f"Reminder: {reminder[1]}")
            reminders.remove(reminder)

# -------------------------
# MAIN FUNCTION
# -------------------------
def run_assistant():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = take_command()

        if "hello" in command:
            speak("Hello! How are you today?")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "date" in command:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {today}")

        elif "search" in command:
            search_term = command.replace("search", "").strip()
            speak(f"Searching {search_term}")
            pywhatkit.search(search_term)

        elif "weather" in command:
            if "in" in command:  # Example: weather in Mumbai
                city = command.split("in")[-1].strip()
                speak(get_weather(city))
            else:
                speak(get_weather("Patan"))

        elif "map" in command and "patan" in command:
            speak("Opening Patan city map.")
            webbrowser.open("https://www.google.com/maps/place/Patan,+Gujarat")

        elif "remind me" in command:
            speak("What should I remind you about?")
            reminder_text = take_command()
            speak("In how many seconds?")
            try:
                seconds = int(take_command())
                set_reminder(reminder_text, seconds)
            except:
                speak("Sorry, I didn't catch the time.")

        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        check_reminders()

# -------------------------
# START
# -------------------------
if __name__ == "__main__":
    run_assistant()
    