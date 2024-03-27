import os, socket, shutil,  time, pprint, threading, datetime,  wave, ner01,ner00
from ast import literal_eval
from gtts import gTTS
from mutagen.mp3 import MP3 as mp3
import speech_recognition as sr
from playsound  import playsound
from multiprocessing import Process, Value
from nltk.tokenize import sent_tokenize
from pydub import AudioSegment
#sound = AudioSegment.from_file("input.mp3", "mp3")
#time = sound.duration_seconds # 再生時間(秒)
HOST = '127.0.0.1'    # The remote host
HOST2= '127.0.0.1'    # The remote host
PORT = 50001 
PORT3= 50003 
PORT11= 500011 
PORT14 = 500014 
PORT16 = 500016 
PORT19= 50019 

r = sr.Recognizer()
mic = sr.Microphone()
s11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s11.bind((HOST, PORT))
s11.listen(1)
from openai import OpenAI

#client = OpenAI(api_key="    -------Own Key------------------9")
#openai.api_key ="      -----------        Own Key           ------------"

import wikipedia as wiki
import pprint as pp
def speed(data,id,speedx):
    af = AudioSegment.from_mp3(data)
    af = af.speedup(playback_speed=speedx, crossfade=0)
    af=af+6
    af.export(data, format="wav")
    if id==1:
        playsound(data)

def Say00(data,id,speedx):
    tts=gTTS(data,lang='ja')
    tts.save('examples/answer.wav')
    speed('examples/answer.wav',id,speedx)

def Say01(data,id,speedx):
    tts=gTTS(data,lang='ja')
    tts.save('question.wav')
    speed('question.wav',id,speedx)

#   os.system('ffmpeg -i answer.wav answer2.wav')
#   with wave.open('./answer2.wav', mode='rb') as wf:
#       print('time(second): ', float(wf.getnframes() / wf.getframerate()))
#       time=float(wf.getnframes() / wf.getframerate())
    time=5
    return time

#   playsound('question.wav')

ss19 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss19.bind((HOST2, PORT19))
ss19.listen(1)

while True:
    print("Say something ...")
    with mic as source:
        r.adjust_for_ambient_noise(source) # for noise
        audio = r.listen(source)
    print ("Now to recognize it...")
    try:
        question=r.recognize_google(audio,language='ja-JP')
        q2='  '+question
        ij=ner01.sub(question) # Detecting phrase , What are you watching
        print(question)
        Say01(q2,1,1.1)
        TP=1.1
        if ij==2:
            word='  '
            question2=word+question+'======================================='
            print(' in IJ==2')

#           s16= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#           s16.connect((HOST2, PORT16))
#           s16.send(question.encode())
#           seeing=s16.recv(4096).decode()
#           s16.close()
            print(' in IJ==2  ')

#           conn19, addr19 = ss19.accept()
#           data = conn19.recv(1024)
#           seeing = data.decode()
#           print('seeing=',seeing)
#           ans99=ner00.trans('EJ',seeing)
#           ans100=ans99+'が見えます。'
#           TP=1.3
#           ij=0
        elif ij==1:
            with open('yahoo/out2_news') as f:
                l = f.readlines()
                print(l)
            text="".join(l)
            print('text=',text)
            ij=0
            TP=1.1
#           text00=text.split('。!?！？')
#           ans100=text00[0]+text00[1]
            ans100='Today\'s news  '+text+'.'
            print(' Today\'s news is ',ans100)
#           ans100=text
        else:
            ij=0

            response = client.chat.completions.create(model='gpt-3.5-turbo',messages=[{ "role":"user","content":question}])
            text=response.choices[0].message.content
            print(' GPT  ====>',text)
            TP=1.40
            text00=text.split('。')
            ans100=text00[0]+text00[1]+text00[2]

        print('ans6======>',ans100)
    
        print("QA 's answer ",ans100)
        time00=Say00(ans100,0, TP )
        print('duration time=',time00)

        time.sleep(18)
    #   time.sleep(data2)
##################################################################################
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

