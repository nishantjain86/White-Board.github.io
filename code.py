import cv2 as cv
import numpy as np
# Create a white board of size 512X512
img = np.ones((512,512,3),np.uint8)*255
#create Green color square
cv.rectangle(img,(41,470),(70,500),(0,255,0),-1)
#create Blue color square
cv.rectangle(img,(71,470),(100,500),(255,0,0),-1)
#create Red color square
cv.rectangle(img,(101,470),(130,500),(0,0,255),-1)
cv.rectangle(img,(131,470),(160,500),(255,255,0),-1)
# create global variables
r=0
g=0
b=0
xi=-1
yi=-1

# Function that writes text on the white board with mouse movement 
def draw_line(event,xf,yf,flags,param):
    # To make sure function do not create new local variables with name r,g, and b , keyword global is used 
    global r,g,b
    # to select the color from color pallete
    if event == cv.EVENT_LBUTTONDBLCLK:
        [b,g,r]=img[yf,xf]
        
    global xi, yi
    # to select the starting point
    if event == cv.EVENT_LBUTTONDOWN:
        xi=xf
        yi=yf
    #To start the drawing
    if event == cv.EVENT_MOUSEMOVE:
        # drawing will start only if xi is not equal to -1. This make sure that drawing will start only after the selection of initial point 
        if(xi !=-1):
            cv.line(img,(xi,yi),(xf,yf),(int(b),int(g),int(r)),3)
            xi=xf
            yi=yf
    # Event left button up will stop the drawing by assigning value -1 to xi
    if event == cv.EVENT_LBUTTONUP:
        xi=-1
        
cv.namedWindow('image')
cv.setMouseCallback('image',draw_line)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
