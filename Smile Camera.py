from SimpleCV import *
import time

dim = {'width': 540, 'height':380}
cam = Camera(0, dim)
count = 0
disp = Display()

try:
    while not disp.isDone():
        img = cam.getImage().flipHorizontal()
        curr = img
        face_segment = HaarCascade("face2.xml")
        gray = curr.grayscale()
        autoface = gray.findHaarFeatures(face_segment)
        facelayer = DrawingLayer(curr.size())
##        facelayer.setFontSize(28)
##        facelayer.text("Whose Birthday is it today ? ", (40, 20), color=Color.RED)
##        curr.addDrawingLayer(facelayer)
        curr.show()
        if autoface is not None:
            face = autoface[-1].boundingBox()
            smile_detect = autoface[-1].crop()
    ##        smile_detect.show()
            
            x, y, w, h = (i for i in face[:4])
            facebox = facelayer.rectangle((x, y), (w, h), color=Color.GREEN, width=2, filled=False)
##            facelayer.text("THIS GUY'S !!", (320, 20), color=Color.RED)
            curr.addDrawingLayer(facelayer)
            curr.applyLayers()
            curr.show()
            smile_segment = HaarCascade("smile1.xml")
            autosmile = smile_detect.findHaarFeatures(smile_segment)

            if autosmile is not None:
                imgname = "SmileImg_"+time.strftime("%Y%m%d%H%M%S")+".jpg"
                path = "D:\\Jay10\\Birthday 2016(Smile Cam)\\"+imgname
                img.save(path)
                time.sleep(0.5)
                count += 1
##                img.show()
                print "Captured and Saved", imgname
                if count > 5:
                    break
                #time.sleep(1)
    disp.quit()
except:
    pass
