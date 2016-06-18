from SimpleCV import *    


cam = Camera() 		# Initialize Camera
img = cam.getImage() 	# get a sample image to know the screen size
display = Display() 	# Creates an object of Display Class
width, height = img.width, img.height 	# Gets width and height of the Image captured
screensize = width*height 	# initialize the screen size
threshold = 200 	    # If value of any pixel goes higher than this, it means light/blob is found in the stream


def onLayer():
    newLayer = DrawingLayer(img.size()) 	# create a pseudo drawing layer
    newLayer.circle((width/2, height/2), width/4, filled=True, color=Color.GREEN) 	# draw a circle at the center of display
    newLayer.setLayerAlpha(75) 	# set transparency of circle
    newLayer.setFontSize(20)
    newLayer.text("Light Detected !", (width/2, height/2), color=Color.WHITE) 	# Display text on the screen

    return newLayer


def offLayer():
    newLayer = DrawingLayer(img.size())
    newLayer.circle((width/2, height/2), width/4, filled=True, color=Color.RED)
    newLayer.setLayerAlpha(75)
    newLayer.setFontSize(20)
    newLayer.text("No Source of Lights found !", (width/2, height/2), color=Color.WHITE)

    return newLayer


while display.isNotDone(): 		# Keeps running till the user presses close button
    img = cam.getImage() 		# Gets image from Camera
    min_blob_size = 0.10*screensize 	# minimum blob size
    max_blob_size = 0.80*screensize	# maximum blob size

    blobs = img.findBlobs(minsize=min_blob_size, maxsize=max_blob_size) # find blobs in the image
    layer = offLayer() 	                # by default, the layer will have no lights

    if blobs: 	                        # but if any blob is found
        avgcolor = np.mean(blobs[-1].meanColor())	# calculate the mean of rgb pixel value of blob

        if avgcolor >= threshold: 	# and if it is greater than threshold value
            layer = onLayer() 		# turn the layer to "on" mode

    img.addDrawingLayer(layer) 		# add layer to the stream
    img.show() 				# show the stream on display

    if display.mouseLeft: 		# stop the streaming if user presses left mouse button
        break
