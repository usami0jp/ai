#https://www.klv.co.jp/corner/python-opencv-video-capture.html
import cv2, time
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera' , frame)
    key =cv2.waitKey(10)
    time.sleep(2)
    pil = Image.fromarray(frame)
    im = np.array(pil)
    pil_img = Image.fromarray(im)
    pil_img.save('image.jpg')

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



'''
import cv2
import random
import numpy as np
from PIL import Image

# Load a speedo image which has transparency
#speedo = Image.open('speedo.png').convert('RGBA')

capture = cv2.VideoCapture("movie.mov")
out = cv2.VideoWriter('test.mov',cv2.VideoWriter_fourcc('a','v','c','1'), 25, (1280, 720))

def velocity():
    now = (random.randint(0,100))
    return now

while True:
    ret, frame = capture.read()
    if ret:
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Orientation:',(15,700),font,0.7,(255,255,255),1)
        cv2.putText(frame, str(velocity()), (130,580),font,0.7,(255,255,255),1)
        cv2.putText(frame,'KM/H',(165,580),font,0.7,(255,255,255),1)

        # Make PIL image from frame, paste in speedo, revert to OpenCV frame
        pilim = Image.fromarray(frame)
        pilim.paste(speedo,box=(80,20),mask=speedo)
        frame = np.array(pilim)

        out.write(frame)
        cv2.imshow("Testing", frame)
        cv2.waitKey(1)

    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
'''
