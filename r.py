import socket,time
from multiprocessing import Process, Value
HOST='127.0.0.1'

HOST2='127.0.0.1'
HOST7='127.0.0.1'

PORT14=50014
PORT15=50015
PORT16=50016
PORT17=50017
PORT19=50019
PORT20=50020

def work17(run,run2):    #   １７　１７
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST2, PORT17))
    s.listen(1)
    print('------------------------ Capturing Camera Image --------------------')
    while True:
        if run.value==1:
            print('------IN ------------------From Voice --------------------')
            s20= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #<==== Transfering to main program
            s20.connect((HOST7, PORT20))
            cue='cue'
            s20.send(cue.encode())

            print(' Camera run.value',run.value)
            conn, addr = s.accept()      # １７　１７
            print( 'Connected by', addr)
            data = conn.recv(1024)
            sentence=data.decode()
            print(sentence)

            s19= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #<==== to Main Program 
            s19.connect((HOST2, PORT19))
            s19.send(sentence.encode())
            s19.close()
            s20.close()

            run.value=0
            print(' End  run.value',run.value)
            print('')


def work16(run,run2):    #　１６　１６
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST2, PORT16))
    s.listen(1)
    print('------OUT------------------From Voice --------------------')
    while True:
        print('----- IN -------------------From Voice --------------------')
        print(run.value)
        conn, addr = s.accept()
        print( 'Connected by', addr)
        data = conn.recv(1024)
        sentence=data.decode()
        print (sentence)
        run.value =1



run = Value("i", 0)  # Start 　１ is out,  ０ is in  #######################
run2= Value("i", 0)

p16= Process(target=work16, args=(run,run2))
p16.start()
p17= Process(target=work17, args=(run,run2))
p17.start()

