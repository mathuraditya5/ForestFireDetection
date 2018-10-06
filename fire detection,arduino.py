
import numpy as nup
import cv2

import time

ramp_frames=30
fire_cascade = cv2.CascadeClassifier('fighter.xml')

cam = cv2.VideoCapture(0)

while 1:
    reet, imgg = cam.read()
    
    white = cv2.cvtColor(imgg,cv2.COLOR_BGR2GRAY)
    red = fire_cascade.detectMultiScale(imgg, 1.2, 5)
    for (x,y,w,h) in red:
        cv2.rectangle(imgg,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = white[y:y+h, x:x+w]
        roi_color = imgg[y:y+h, x:x+w]
        time.sleep(0.2)
        
    cv2.imshow('imgg',imgg)
    def get_image():
    
     retval, im = cam.read()
      
     return im
     for i in range(ramp_frames):
      temp = get_image()
    print("Taking image...")
    camera_capture = get_image()
    file = "C:\\Users\\DIVYANSHU VYAS\\Documents\\Hackathon\\test_image.png"
    cv2.imwrite(file, camera_capture)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
 


cam.release()
cv2.destroyAllWindows()
