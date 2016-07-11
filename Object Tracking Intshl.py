from SimpleCV import *

cam = Camera(0 ,{'width': 640, 'height': 480})
disp = Display()
img = cam.getImage()
size = img.size()
img_width, img_height = img.width, img.height

HUE = 40

disp = Display()


def print_position(x, y, size):
    newLayer = DrawingLayer(size)
    newLayer.centeredRectangle((100, 50), (200, 100), filled=True, color=Color.WHITE)
    newLayer.setLayerAlpha(45)

    ball_x = "x: "+str(x)
    ball_y = "y: "+str(y)

    newLayer.text(ball_x, (20, 20), color=Color.BLACK)
    newLayer.text(ball_y, (20, 40), color=Color.BLACK)

    newLayer.circle((x, y), 50, width=10, color=Color.RED)

    return newLayer


while not disp.isDone():
    img = cam.getImage().flipHorizontal()
    hsv_img = img.toHSV()
    dist_img = hsv_img.hueDistance(HUE)
##    dist_img.show()
    bin_img = dist_img.binarize(20)
##    bin_img.show()
    eroded_img = bin_img.erode()
    dilated_img = eroded_img.dilate()
    blobs = dilated_img.findBlobs()

    if blobs:
        blob_center = blobs[-1].centroid()
        x, y = int(blob_center[0]), int(blob_center[1])
        layer = print_position(x, y, img.size())
        img.addDrawingLayer(layer)

    img.show()
