from tkinter import *
import wikipedia
import speech_recognition as sr
import gui

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
            root.destroy()
            return

        try:
            answer = wikipedia.summary(text)
            response_text.config(state=NORMAL)
            response_text.delete(1.0, END)
            response_text.insert(END, "Answer from Wikipedia:\n" + answer)
            response_text.config(state=DISABLED)
            print("Answer from Wikipedia:")
            print(answer)
        except wikipedia.exceptions.DisambiguationError as e:
            response_text.config(state=NORMAL)
            response_text.delete(1.0, END)
            response_text.insert(END, "There are multiple results for this query. Please be more specific.")
            response_text.config(state=DISABLED)
            print("There are multiple results for this query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            response_text.config(state=NORMAL)
            response_text.delete(1.0, END)
            response_text.insert(END, "No results found on Wikipedia. Please try again.")
            response_text.config(state=DISABLED)
            print("No results found on Wikipedia. Please try again.")

    except TimeoutError:
        print("No speech detected. Please try again.")
        response_text.config(state=NORMAL)
        response_text.delete(1.0, END)
        response_text.insert(END, "No speech detected. Please try again.")
        response_text.config(state=DISABLED)

    except sr.RequestError:
        print("Could not request results. Please check your internet connection.")
        response_text.config(state=NORMAL)
        response_text.delete(1.0, END)
        response_text.insert(END, "Could not request results. Please check your internet connection.")
        response_text.config(state=DISABLED)

    except Exception as e:
        error_message = "Sorry, I couldn't understand you clearly. Can you please rephrase your question?"
        response_text.config(state=NORMAL)
        response_text.delete(1.0, END)
        response_text.insert(END, error_message)
        response_text.config(state=DISABLED)
        print(error_message)
        print(e)

if __name__ == "__main__":
    root, response_text = gui.setup_gui(listen_and_respond)
    root.mainloop()
