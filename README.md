# Eve_Voice_Assistant
Eve is a fully offline AI voice assistant powered by GPT4All. She features real-time voice recognition, synthesized voice output, and animated 2D sprites using a Tkinter-based GUI.
---

## Features

- Offline AI with GPT4All (No Internet Required)
- Always-listening speech recognition
- Real-time AI response generation
- Text-to-speech output with animated sprite
- Interrupt speech anytime by saying "stop"
- Animated 2D assistant using sprite sheets
- Open source and fully customizable

---

## Technologies Used

- Python 3.10.0 (older version used because some libraries didn't support current py version)
- GPT4All (Llama 3.2B GGUF model)
- Tkinter for GUI
- PIL for image animation
- pyttsx3 and win32com for TTS
- SpeechRecognition for voice input

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/eve-voice-assistant.git
cd eve-voice-assistant
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv rasa_env
rasa_env\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Place Your Assets
- Download the Llama GGUF model (e.g., `Llama-3.2-3B-Instruct-Q4_0.gguf`) from GPT4All.
- Place it in the `models/` directory.
- Put sprite PNGs into the `sprites/` folder (named sequentially like `frame_0.png`, `frame_1.png`, etc).
- Optional: Add GUI images or a banner in the `assets/` folder.

### 5. Run the Assistant
1. firstly setup two command prompt windows
2. then in first CL add the path of your "rasa_proj" (eg:"C:\Users\Gurucharan\Downloads\chatbot\rasa_proj")
3. after path make it run in rasa env using "rasa_env\scripts\activate" (make sure u do this before "cd rasa_proj") after this type "rasa run"
4. same follows for "rasa_code"
5. "(rasa_env) C:\Users\Gurucharan\Downloads\chatbot\rasa_code>" it looks like this (type "python voice_bot.py")

```bash
python voice_bot.py
```
###installations pip
pip install pillow
pip install SpeechRecognition
pip install pyttsx3
pip install gpt4all
pip install pywin32  # For win32com.client
pip install pyautogui  # Optional for mouse control

###installations rasa
pip install rasa
rasa init #create new proj
rasa train #train model
rasa shell #test model


## Roadmap
- [x] Voice recognition
- [x] GPT4All integration
- [x] Sprite-based animation
- [x] Text display during speech
- [x] Interrupt speech with "stop"
- [ ] Frame-by-frame lipsync
- [ ] Add mouse control and file operation support

---

## Credits
- Sprites provided by contributors on Itch.io (Free Pixel Packs)
- GPT4All team for the model and API: https://gpt4all.io

---

## Support 

Support me on 
Linkedin: "https://www.linkedin.com/in/gurucharan-s-31310324b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BuOyVAY5ES3OGNOsMmf3h6g%3D%3D"
instagram: @_charanu__
If you like this project, please consider giving it a star and connecting on LinkedIn.

---
## Any upgrades or changes kindly feel free to ping me on "gurucharan87318@gmail.com"

