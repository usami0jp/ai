import requests, cv2, time
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
import numpy as np
import socket, time
from multiprocessing import  Process, Value

HOST7='127.0.0.1'
HOST10='127.0.0.1'

PORT15=50015
PORT17=50017
PORT18=50018
PORT19=50019
PORT20=50020
run=Value("i",0)
run2=Value("i",0)
#s20= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s20.bind((HOST10, PORT20))
#s20.listen(1)
def worker(run,run2):
    s20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s20.bind((HOST7, PORT20))
    s20.listen(1)
    print('------------------------waiting for input --------------------')
    while True:
        print(' in  ',run.value)
        conn, addr = s20.accept()
        print( 'Connected by', addr)
        run.value=1
        data = conn.recv(1024)
        print (data.decode())
        conn.close() #　　＜ーーーーーーーーここが重要　上は無関係
#       image = Image.open("image.jpg")
#       image.show()
        imgCV=cv2.imread('image.jpg')
        cv2.namedWindow("window-name", cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMALの値は0なので0を指定してもよい
        cv2.imshow("window-name", imgCV)

#       print(' in  ',run.value)

p0=Process(target=worker, args=(run,run2))
p0.start()

def image2text(run,run2):
    model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224")
    processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0)
    prompt = "<grounding>An image of"
    while True:
        ret, frame = cap.read()
        height = frame.shape[0]
        width = frame.shape[1]
        frame2 = cv2.resize(frame,(width*2, height*2))
        cv2.imshow('camera' , frame2)
        key =cv2.waitKey(10)
        pil = Image.fromarray(frame)
        im = np.array(pil)
        pil_img = Image.fromarray(im)
        pil_img.save('image.jpg')
#       image = Image.open("image.jpg")
        image=pil_img
#       print(' out  ',run.value)
#       time.sleep(1)
#       image.show()
        if run.value==1:
            print(' out out out  ',run.value)
            inputs = processor(text=prompt, images=image, return_tensors="pt")
            generated_ids = model.generate(
                    pixel_values=inputs["pixel_values"],
                    input_ids=inputs["input_ids"],
                    attention_mask=inputs["attention_mask"],
                    image_embeds=None,
                    image_embeds_position_mask=inputs["image_embeds_position_mask"],
                    use_cache=True,
                    max_new_tokens=128,
                    )
            generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    ####    processed_text = processor.post_process_generation(generated_text, cleanup_and_extract=False)
            processed_text, entities = processor.post_process_generation(generated_text)
#           print(processed_text,entities)
            print(processed_text)
        
            s17 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s17.connect((HOST10, PORT17))
            s17.send(processed_text.encode())
            s17.close()
#           time.sleep(3)
            run.value=0
            print(' out out out  ',run.value)
    
#       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#       s.connect((HOST10, PORT15))
#       s.send(processed_text.encode())
#       s.close()
#       time.sleep(0)
    
p = Process(target=image2text, args=(run,run2))
p.start()
