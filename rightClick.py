import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if(event == cv2.EVENT_RBUTTONDOWN):
        cv2.circle(img,(x,y),100,(255,0,0),thickness=10)
cv2.namedWindow(winname = 'drawing')
cv2.setMouseCallback('drawing',draw_circle)

img = cv2.imread('../DATA/dog_backpack.png')

while True:
    cv2.imshow('drawing',img)
    if(cv2.waitKey(2) & 0xFF == 27):
        break
cv2.destroyAllWindows()