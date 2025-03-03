import cv2
import numpy as np
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    # Optionally flip the frame to avoid inverse reactions
    frame = cv2.flip(frame, 1)  # Flip the image horizontally (use 0 for vertical flip if needed)

    # Decode QR/barcodes in the frame
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data.decode())
        # Display the data on the frame
        cv2.putText(frame, str(obj.data.decode()), (50, 50), font, 3, (255, 0, 0), 3)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Wait for the user to press the ESC key to exit
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
