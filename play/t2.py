from moviepy.editor import *
from multiprocessing import Process, Value
import time,pygame
import moviepy


def work16(run,run2):
    clip=VideoFileClip('./out.mp4')
    clip=clip.resize(4)
    clip.preview()
    time.sleep(1)
    pygame.quit()

def work17(run,run2):
    time.sleep(3)
    clip2=VideoFileClip('./out2.mp4')
    clip2=clip2.resize(4)
    clip2.preview()




    

run = Value("i", 0)  
run2= Value("i", 0)

p16= Process(target=work16, args=(run,run2))
p16.start()
#p17= Process(target=work17, args=(run,run2))
#p17.start()


