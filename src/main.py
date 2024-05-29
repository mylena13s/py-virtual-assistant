import wikipedia
import speech_recognition as sr
import gui
import sys
from PySide6.QtWidgets import QApplication

def listen_and_respond(response_text):
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
            response_text.setPlainText("Answer from Wikipedia:\n" + answer)
            print("Answer from Wikipedia:")
            print(answer)
        except wikipedia.exceptions.DisambiguationError as e:
            response_text.setPlainText("There are multiple results for this query. Please be more specific.")
            print("There are multiple results for this query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            response_text.setPlainText("No results found on Wikipedia. Please try again.")
            print("No results found on Wikipedia. Please try again.")

    except TimeoutError:
        print("No speech detected. Please try again.")
        response_text.setPlainText("No speech detected. Please try again.")

    except sr.RequestError:
        print("Could not request results. Please check your internet connection.")
        response_text.setPlainText("Could not request results. Please check your internet connection.")

    except Exception as e:
        error_message = "Sorry, I couldn't understand you clearly. Can you please rephrase your question?"
        response_text.setPlainText(error_message)
        print(error_message)
        print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window, response_text = gui.setup_gui(listen_and_respond)
    sys.exit(app.exec())
