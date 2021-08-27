import cv2
import time
import numpy as np
import hand_detect as hd
from model import SignDetec

model = SignDetec('../models/model.h5')

wCam, hCam = 800, 600

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = hd.handDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, center = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        cv2.circle(img, tuple(center), 10, (0, 0, 255), 1)
        cv2.rectangle(img, (center[0]-150, center[1]-170), (center[0]+150, center[1]+170), (0, 255, 0), 1)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_hi = gray_img[center[1]-170:center[1]+170, center[0]-150:center[0]+150]

        try:
            img2pred = cv2.resize(img_hi, (28,28))
            pred = model.predict_sing(img2pred[np.newaxis, :, :, np.newaxis])
            print(pred)

            cv2.putText(img, pred, (center[0]-150, center[1]-150),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        except Exception as e:
            pass

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    try:
        cv2.imshow("Hand", img_hi)
    except Exception as e:
        pass
    cv2.waitKey(1)