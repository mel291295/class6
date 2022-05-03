#! python3

from googletrans import Translator
from gtts import gTTS
import streamlit as st

user_text = st.text_input("Give me some text you want me to translate in English and read for you: ")

# It then converts that text in a certain langauge

translator = Translator()
text_to_translate = translator.translate(text=user_text, dest='en')

text_to_speech = text_to_translate.text
st.write(text_to_speech)
# it converts the translated text to speech.
tts=gTTS(text=text_to_speech, lang='en')

tts.save('audio.mp3')

st.write("Your text would sound like this in English:")
audio_file = open('audio.mp3', 'rb')
st.audio(data=audio_file, format="audio/mp3", start_time=0)
