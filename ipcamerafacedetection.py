import cv2
import urllib 
import numpy as np
#for windows
face_cascade = cv2.CascadeClassifier('C:\\Users\\your user\\Downloads\\cv\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
#for linux
#face_cascade = cv2.CascadeClassifier('/root/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
stream=urllib.urlopen('http://174.6.126.86/mjpg/video.mjpg?COUNTER')
#i1 = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if faces != ():
            for (x,y,w,h) in faces:            
                cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = i[y:y+h, x:x+w]
                #eyes = eye_cascade.detectMultiScale(roi_gray)
                #for (ex,ey,ew,eh) in eyes:
                 #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.namedWindow('i1',16)                         
        cv2.imshow('i1',i)
        cv2.moveWindow('i1',300,300)
        cv2.resizeWindow('i1',600,400)
        if cv2.waitKey(1) ==27:
            exit(0)  
