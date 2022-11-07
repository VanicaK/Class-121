import cv2
import mediapipe as mp


mpdrawing=mp.solutions.drawing_utils
mphands=mp.solutions.hands
hands=mphands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
tipids=[4,8,12,16,20]

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    image=cv2.flip(image,1)
    results=hands.process("image")


    cv2.imshow("Media Controller", image)
    

    key = cv2.waitKey(1)
    if key == 32:
        break

    

cv2.destroyAllWindows()

def drawLandmarks(image,hand_landmarks):
    if(hand_landmarks):
       for landmarks in hand_landmarks:
            mpdrawing.draw_landmarks(image,landmarks,mp_hands.handconnections)
    for tips in hand_landmarks:
        if(hand_landmarks):
            for landmarks in hand_landmarks:
                mpdrawing.draw_landmarks(image,landmarks,mphands.handconnections)

