from gtts import gTTS
import os
from playsound import playsound

def yazidan_sese(dil, yazi, dosya_ismi):
    tts = gTTS(text=yazi, lang=dil)
    tts.save(dosya_ismi)
    playsound(dosya_ismi)

if __name__ == "__main__":
    dil = input("Yazı Dili(tr, en, es vb.): ")
    yazi = input("Yazı: ")
    dosya_ismi = input("Kaydedilecek dosyanın ismi(merhaba.mp3 gibi): ")
    yazidan_sese(dil, yazi, dosya_ismi)