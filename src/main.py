import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr

def listen_and_respond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello, I'm listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: ' + text)

        if text.lower() == "stop":
            print("The program will exit.")
            root.destroy()  
            return

        app_id = "Q6AA9P-KKLX2VEQ76"
        client = wolframalpha.Client(app_id)
        res = client.query(text)

        answer = next(res.results).text
        response_label.config(text="Answer from Wolfram|Alpha:\n" + answer)
        print("Answer from Wolfram|Alpha:")
        print(answer)

    except wolframalpha.Client.RequestError:
        print("No results from Wolfram|Alpha. Trying Wikipedia...")
        answer = wikipedia.summary(text)
        response_label.config(text="Answer from Wikipedia:\n" + answer)
        print("Answer from Wikipedia:")
        print(answer)

    except Exception as e:
        error_message = "Sorry, I couldn't understand you clearly. Can you please rephrase your question?"
        response_label.config(text=error_message)
        print(error_message)
        print(e)

# Estrutura básica da GUI
root = Tk()
root.title("Virtual Assistant")

# Label para exibir as respostas
response_label = Label(root, text="", wraplength=400)
response_label.pack(pady=10)

# Botão para ouvir e responder
listen_button = Button(root, text="Listen", command=listen_and_respond)
listen_button.pack(pady=10)

root.mainloop()
