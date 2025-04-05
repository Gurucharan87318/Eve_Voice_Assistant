import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading
import speech_recognition as sr
import time
import os
import win32com.client
from gpt4all import GPT4All

# ===== Initialize GPT4All Model =====
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=r"C:\Users\Gurucharan\Downloads\gpt4all")

# ===== Setup GUI =====
window = tk.Tk()
window.title("Eve - Voice Assistant")
window.geometry("600x600")

# Sprite Animation Frames
sprite_names = sorted([f for f in os.listdir() if f.endswith(".png")])
sprites = [ImageTk.PhotoImage(Image.open(name).resize((300, 300))) for name in sprite_names]

sprite_index = 0
animation_label = tk.Label(window)
animation_label.pack(pady=10)

# Spoken Text Display
speech_text_label = tk.Label(window, text="", font=("Helvetica", 14), fg="blue")
speech_text_label.pack()

# Chat Box
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state="disabled", font=("Helvetica", 12), height=15)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# ===== Speaking and Animation =====
talking = False


def animate():
    global sprite_index
    if talking:
        sprite_index = (sprite_index + 1) % len(sprites)
        animation_label.config(image=sprites[sprite_index])
    window.after(100, animate)


speaker = win32com.client.Dispatch("SAPI.SpVoice")
for voice in speaker.GetVoices():
    if "zira" in voice.GetDescription().lower():
        speaker.Voice = voice
        break

def speak(text):
    global talking
    talking = True
    update_chat("Eve", text)
    speech_text_label.config(text=text)
    speaker.Speak(text)
    time.sleep(1.5)
    talking = False
    speech_text_label.config(text="")


def update_chat(sender, text):
    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"{sender}: {text}\n")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)


# ===== Ask GPT4All =====
def ask_local_ai(prompt):
    with model.chat_session():
        return model.generate(prompt, max_tokens=100).strip()


# ===== Voice Listening Loop =====
def listen_loop():
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            update_chat("You", command)

            # GPT4All Response
            response = ask_local_ai(command)
            speak(response)

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Microphone or speech service error.")


# ===== Start Background Tasks =====
def start_background_tasks():
    threading.Thread(target=listen_loop, daemon=True).start()
    animate()


# ===== Run App =====
speak("Hello! I am Eve. How can I help you?")
start_background_tasks()
window.mainloop()
