import cv2 
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)

while True:
    ret , frame = cap.read() 
    frame , faces = detector.findFaceMesh(frame)
    cv2.imshow("webcam" , frame)
    if cv2.waitKey(1) & 0xFF == ord('x'): 
        break

cap.release() 
cv2.destroyAllWindows()