# program to detect face in an image
# cv2 needs to be installed, the terminal command is pip3 install cv2
import cv2
# import the xml file
# an xml file which helps the program in reading the faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# read the image to be tested
img = cv2.imread('test.jpg')

#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLORR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# add rectangle around the detected faces
for (x,y,w,h) in faces:
    cv2.rectange(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
    
# show the picture and save it in the directory as face_detected.jpg
cv2.imshow('img', img)
cv2.waitKey()

cv2.imwrite('face_detected.jpg', img)