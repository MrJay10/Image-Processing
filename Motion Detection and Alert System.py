import time
from SimpleCV import *
import pygame

cam = Camera(0, {'width': 640, 'height': 480})
threshold = 4.5
disp = Display((640, 480))
previous = cam.getImage()
flag = False

def motion_layer():
    
    newLayer = DrawingLayer(previous.size())
    width, height = previous.width, previous.height
    newLayer.centeredRectangle((width/2, height/2), (200, 200), filled=True, color=Color.RED)
    newLayer.setLayerAlpha(75)
    newLayer.setFontSize(20)
    newLayer.text("ALERT !!!", (width/2-25, height/2))

    return newLayer

while not disp.isDone():
    time.sleep(0.2)
    curr = cam.getImage()
    diff = curr - previous
    matrix = diff.getNumpy()
    mean = matrix.mean()
    print mean

    if mean >= threshold:
        print "Greater", mean
        print "There has been a motion !!"
        layer = motion_layer()
        flag = True
        break

    else: curr.show()
    previous = curr

if flag:
    curr.addDrawingLayer(layer)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Alert.wav")
    pygame.mixer.music.play(-1)
    try:
        while not disp.isDone():
            curr.show()
            curr.save('C:/Python27/Simplecv/Movement Detected/Motion.jpg')
    except:
        pass
