import speech_recognition as sr
import threading,datetime,time, socket
HOST = '127.0.0.1'    # The remote host
PORT = 50014 # The same port as used by the server

r = sr.Recognizer()
mic = sr.Microphone()
time00=time.time()



while True:
    print("Say something ...")
    print(time.time()-time00)
    time00=time.time()
    print('in ------',time.time()-time00)


    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)
    print ("Now to recognize it...")
    try:
#       aa=r.recognize_google(audio, language='ja-JP')
        aa=r.recognize_google(audio)
        print(aa)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(aa.encode())
        s.close()

    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


