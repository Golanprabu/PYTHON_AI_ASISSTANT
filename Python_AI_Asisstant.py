import speech_recognition as sr
import pyttsx3
import wikipedia

# Inisialisasi library speech recognition dan text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Setel penyesuaian untuk noise lingkungan
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError:
        print("There was an error with the speech recognition service. Please check your internet connection or try again later.")
        return ""

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def assistant_logic(command):
    if "hello" in command.lower():
        return "Hello! How can I assist you?"
    elif "what is your name" in command.lower():
        return "I am your AI Assistant."
    elif "search" in command.lower():
        search_query = command.lower().replace("search", "").strip()
        try:
            search_results = wikipedia.summary(search_query, sentences=2)
            return f"Here is a summary: {search_results}"
        except wikipedia.exceptions.PageError:
            return f"Sorry, I couldn't find any information on {search_query}."
    elif "exit" in command.lower():
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that command."

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()
        if "exit" in user_input.lower():
            speak("Goodbye!")
            break
        response = assistant_logic(user_input)
        print("AI:", response)
        speak(response)
