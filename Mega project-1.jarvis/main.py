import speech_recognition as sr
import pyttsx3
import webbrowser
import musicaLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "d093053d72bc40248998159804e0e67d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def process_command(c):
    c = c.lower()

    if "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")

    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")

    elif c.startswith("play "):
        song = c.split(" ")[1]
        link = musicaLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found")

    elif "news" in c:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:
                speak(article["title"])

    else:
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

        command = recognizer.recognize_google(audio)

        if command.lower() == "jarvis":
            speak("Yes, how can I help you?")

            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            process_command(command)

    except Exception as e:
        print("Error:", e)
