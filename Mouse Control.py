from SimpleCV import *
from pymouse import PyMouse

m = PyMouse()
desktop_size = m.screen_size()
desk_width, desk_height = desktop_size[0], desktop_size[1]

cam = Camera(0, {'width': 640, 'height': 480})
img = cam.getImage()
img_width, img_height = img.width, img.height

wd_conv = float(desk_width/img_width)
ht_conv = float(desk_height/img_height)

HUE = 40 	## Mouse will track green color on screen

disp = Display()
while not disp.isDone():
    img = cam.getImage().flipHorizontal()
    hsv_img = img.toHSV()
    dist_img =hsv_img.hueDistance(HUE)
    bin_img = dist_img.binarize(20)
    eroded_img = bin_img.erode()
    dilated_img = eroded_img.dilate()

    blobs = dilated_img.findBlobs()
    img.show()

    if blobs:
        blob_center = blobs[-1].centroid()
        x = int(blob_center[0]*wd_conv)
        y = int(blob_center[1]*ht_conv)
        m.move(x, y)
