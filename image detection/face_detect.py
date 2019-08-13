import cv2
import numpy as np

# face_cas = cv2.CascadeClassifier('cascade_face.xml')

eye_cas = cv2.CascadeClassifier('cascade_eye.xml')

img = cv2.imread("man.jpeg", 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = eye_cas.detectMultiScale(img_gray, scaleFactor= 1.05, minNeighbors=5)

print(type(faces))
print (faces)

for a,b,w,h in faces:
    img = cv2.rectangle(img, (a,b), (a+w,b+h), (0,255,0), 3)

# resized = cv2.resize(img, (int(img.shape[1]), int (img.shape[0])))


cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

