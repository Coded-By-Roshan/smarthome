import pyttsx3
from gtts import gTTS
 
audio_text = "this is good"
engine = pyttsx3.init()
file_path = "roshan.mp3"
tts = engine.getProperty('voice')
tts = gTTS(audio_text)
engine.save_to_file(audio_text, file_path)
print("saved")
engine.runAndWait()