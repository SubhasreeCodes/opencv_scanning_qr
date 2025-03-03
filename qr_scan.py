import cv2
import numpy as np
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)
font= cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        # print("Data", obj.data.decode())
        cv2.putText(frame, str(obj.data.decode()), (50,50),font, 3, (255, 0, 0),3 )


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
