import cv2 as cv 

img = cv.imread("people.jpg")
img_gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("window" , img_gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(img_gray , scaleFactor=1.1 , minNeighbors=15)
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y) , (x+w,y+h),color=(0,255,0), thickness=1 )
cv.imshow("Detected" , img)
cv.waitKey(0)