import cv2,time
class App:
    def __init__(self):
        self.windowName_in = "VIDEO IN"
        cv2.namedWindow(self.windowName_in)
        cv2.namedWindow(self.windowName_in2)
        self.frame_num = 0
        
    def openVideo(self):
        def getFps():
            fps = self.src.get(cv2.CAP_PROP_FPS)
            frame_time = int(1 / fps * 1000 )
            return fps, frame_time
            
        self.src = cv2.VideoCapture('out.mp4')
        self.src2 = cv2.VideoCapture('out2.mp4')
        self.fps, self.frame_time = getFps()

        print('FPS = ', self.fps)
        print('FRAME_TIME = ', self.frame_time)
        
    def playVideo(self):
        def initFrame():
            retval, frame = self.src.read()
            h, w, channels = frame.shape
            return h, w, frame
        
        def initWriter():
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            rec = cv2.VideoWriter('video_out.mp4', fourcc, self.fps, (w, h))
            return rec
        
        h, w, frame = initFrame()
        rec = initWriter()
        
        while True:
            retval, frame = self.src.read()
            retval2, frame2 = self.src2.read()
            
            cv2.imshow(self.windowName_in, frame)
            time.sleep(3)
            cv2.imshow(self.windowName_in, frame2)
        
            key = cv2.waitKey(self.frame_time)
            if key == 27:
                print("ESC CLICKED..")
                break
            
            self.frame_num += 1
            
    def closeVideo(self):
        cv2.destroyAllWindows()
        self.src.release()
            
    def run(self):
        self.openVideo()
        self.playVideo()
        self.closeVideo()

class Util:
    def msg():
        print("hoge")
        
if __name__ == '__main__':
    App().run()
