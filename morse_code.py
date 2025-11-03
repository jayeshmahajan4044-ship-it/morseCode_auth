import cv2 
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import time


# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

morse_sequence = ""     # current sequence 
decoded_message = ""    # full message
blink_start_time = 0
last_blink_time = time.time()
blink_in_progress = False
dot_dash_threshold = 0.4 # seconds
letter_gap = 2.0           # seconds
word_gap = 5.0             # seconds

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
plotY = LivePlot(640 , 360 , [20 , 50], invert=True)
blinkCounter = 0
counter = 0


idList = [22,23,24,26,110,157,158,159,160,161,130 , 243]
ratioList = []
while True:
    ret , frame = cap.read() 
    frame , faces = detector.findFaceMesh(frame,draw=False)
    if faces:
        face=faces[0]
        for id in idList:
            cv2.circle(frame , face[id], radius=2,color= (255 ,0 ,255),thickness=-1)
        
        leftup = face[159]
        leftdown = face[23]
        leftleft = face[130]
        leftright = face[243]
        length_ver , _ = detector.findDistance(leftup,leftdown)
        length_hor, _ = detector.findDistance(leftleft,leftright)

        cv2.line(frame , leftup,leftdown , (0,200,0),2)
        cv2.line(frame , leftleft,leftright , (0,200,0),2)

        ratio = int((length_ver/length_hor)*100)
        ratioList.append(ratio)
        if len(ratioList)>5:
            ratioList.pop(0)
        
        ratioAvg = sum(ratioList)/len(ratioList)
        
        if ratioAvg<32 and counter ==0:
            blinkCounter +=1
            counter = 1
        
        if counter !=0:
            counter +=1
            if counter >15:
                counter= 0

        cv2.putText(frame, f'Blink Counter: {blinkCounter}', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


        imgPlot = plotY.update(ratioAvg)
    
        imgStack =cvzone.stackImages([frame, imgPlot], 2 ,1)

    current_time = time.time()

    if ratioAvg < 32 and counter == 0:
        blink_start_time = current_time
        blink_in_progress = True
        counter = 1

    if counter != 0:
        counter += 1
        if counter > 15:
            counter = 0

    if blink_in_progress and ratioAvg > 32:  # Blink ended
        blink_duration = current_time - blink_start_time
        if blink_duration < dot_dash_threshold:
            morse_sequence += "."
        else:
            morse_sequence += "-"
        print("Morse Seq:", morse_sequence)
        last_blink_time = current_time
        blink_in_progress = False

    # Check if it's time to end a letter or word
    time_since_last_blink = current_time - last_blink_time

    if morse_sequence and time_since_last_blink > letter_gap:
        if time_since_last_blink < word_gap:
            # End of letter
            decoded_char = MORSE_CODE_DICT.get(morse_sequence, '?')
            decoded_message += decoded_char
            print("Decoded so far:", decoded_message)
        else:
            # End of word
            decoded_char = MORSE_CODE_DICT.get(morse_sequence, '?')
            decoded_message += decoded_char + " "
            print("Decoded so far:", decoded_message)
        morse_sequence = ""


    cv2.putText(frame, f'Morse: {morse_sequence}', (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(frame, f'Message: {decoded_message}', (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)


    cv2.imshow("webcam" , imgStack)
    if cv2.waitKey(1) & 0xFF == ord('x'): 
        break

cap.release() 
cv2.destroyAllWindows()





