import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, timeout=3, phrase_time_limit=3)
val=r.recognize_google(audio, language='zh-TW')
print(val)
                   
#r.recognize_google(audio, language='zh-TW')
''' test to print
print()
for data in val:
    print(str(data),end='')
'''
from gtts import gTTS  #文字轉換成mp3
from pygame import mixer #mixer有方法讓音檔播放
mixer.init() #初始化音訊

import tempfile #暫存

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp: #使用完檔案後刪除
        tts = gTTS(text=sentence, lang='zh-TW') #變數存到暫存檔
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
speak(str(val)) 
