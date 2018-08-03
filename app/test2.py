from gtts import gTTS
text ="떡볶이"

tts = gTTS(text=text, lang='ko')
tts.save("sample.mp3")