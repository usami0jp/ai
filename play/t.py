import cv2,time

path = r'out.mp4'
cap = cv2.VideoCapture(path)

i=1
while True :
    print("Frame: "+ str(i))
    #フレーム情報取得
    ret, img = cap.read()
    
    #動画が終われば処理終了
    if ret == False:
        break
    

    #動画表示
    cv2.imshow('Video', img)
    i +=1
    time.sleep(7)

    
cap.release()
cv2.destroyAllWindows()
