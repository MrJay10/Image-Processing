from SimpleCV import *
from pykeyboard import PyKeyboard
import time

cam = Camera(0, {'width': 320, 'height': 240})
## disp = Display()
paused = False
k = PyKeyboard()

##while not disp.isDone():
while True:
    img = cam.getImage().flipHorizontal()
    face_segment = HaarCascade("face.xml")
    gray = img.grayscale()
    autoface = gray.findHaarFeatures(face_segment)

    if autoface is not None:
##        face = autoface[-1].boundingBox()
##        x, y, w, h = (i for i in face[:4])
##
##        facelayer = DrawingLayer(img.size())
##        facebox = facelayer.rectangle((x, y), (w, h), color=Color.GREEN, width=2, filled=False)
##
##        img.addDrawingLayer(facelayer)
##        img.applyLayers()

##        img.show()

        if paused:
            k.tap_key(k.space_key)
            paused = False

    elif not paused:
        k.tap_key(k.space_key)
        paused = True
