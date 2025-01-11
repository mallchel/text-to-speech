from gtts import gTTS

with open('assets/sample1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 'en': English language.
# 'com': Standard English voice.
# 'False': Normal speed.
tts = gTTS(text, lang='en', tld='com', slow=False)
tts.save("assets/sample1.mp3")

print("Saved as 'assets/sample1.mp3'")
