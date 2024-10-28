import wikipedia
import speech_recognition as sr
import sys
from PySide6.QtWidgets import QApplication

def listen_and_respond():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Hello, I'm listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5)
            print("Audio captured. Processing...")
            
        text = r.recognize_google(audio, language='en-US')
        print("You said: " + text + "?")

        if text.lower() == "stop":
            print("The program will exit.")
            QApplication.quit()
            return

        try:
            answer = wikipedia.summary(text)
            print("Answer from Wikipedia:")
            print(answer)
        except wikipedia.exceptions.DisambiguationError as e:
            print("There are multiple results for this query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("No results found on Wikipedia. Please try again.")

    except TimeoutError:
        print("No speech detected. Please try again.")

    except sr.RequestError:
        print("Could not request results. Please check your internet connection.")

    except Exception as e:
        error_message = "Sorry, I couldn't understand you clearly. Can you please rephrase your question?"
        print(error_message)
        print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listen_and_respond()
    sys.exit(app.exec())
