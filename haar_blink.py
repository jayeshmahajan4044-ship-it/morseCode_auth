import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

# Load Haar Cascade for Eye Detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
plotY = LivePlot(640 , 360 , [20 , 50] )
blinkCounter = 0
counter = 0

idList = [22,23,24,26,110,157,158,159,160,161,130 , 243]
ratioList = []

while True:
    ret , frame = cap.read()
    frame , faces = detector.findFaceMesh(frame,draw=False)

    # Convert to grayscale for Haar Cascade eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame for Haar Cascade
    faces_haar = eye_cascade.detectMultiScale(gray, 1.1, 4)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(frame , face[id], radius=2,color= (255 ,0 ,255),thickness=-1)

        leftup = face[159]
        leftdown = face[23]
        leftleft = face[130]
        leftright = face[243]
        length_ver , _ = detector.findDistance(leftup,leftdown)
        length_hor, _ = detector.findDistance(leftleft,leftright)

        cv2.line(frame , leftup, leftdown , (0,200,0),2)
        cv2.line(frame , leftleft, leftright , (0,200,0),2)

        ratio = int((length_ver / length_hor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 5:
            ratioList.pop(0)

        ratioAvg = sum(ratioList) / len(ratioList)

        if ratioAvg < 32 and counter == 0:
            blinkCounter += 1
            counter = 1

        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0

        cv2.putText(frame, f'Blink Counter: {blinkCounter}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        imgPlot = plotY.update(ratioAvg)
        cv2.imshow("plot", imgPlot)
        imgStack = cvzone.stackImages([frame, imgPlot], 2, 1)

    # Loop through each detected face in Haar Cascade and draw rectangles around eyes
    for (x, y, w, h) in faces_haar:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("webcam", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
