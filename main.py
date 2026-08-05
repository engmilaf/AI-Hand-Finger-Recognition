import cv2
import mediapipe as mp


# تشغيل الكاميرا
cap = cv2.VideoCapture(0)


# إعداد MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils


# أسماء الأصابع
finger_names = [
    "Thumb",
    "Index",
    "Middle",
    "Ring",
    "Pinky"
]


while True:

    success, img = cap.read()

    if not success:
        break


    # تحويل الصورة إلى RGB
    imgRGB = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )


    # اكتشاف اليد
    results = hands.process(imgRGB)


    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:


            landmarks = []


            for id, lm in enumerate(handLms.landmark):

                h,w,c = img.shape

                cx = int(lm.x*w)
                cy = int(lm.y*h)

                landmarks.append((cx,cy))


            fingers = []


            # الإبهام
            if landmarks[4][0] < landmarks[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)


            # باقي الأصابع
            tips = [8,12,16,20]


            for tip in tips:

                if landmarks[tip][1] < landmarks[tip-2][1]:
                    fingers.append(1)

                else:
                    fingers.append(0)



            count = fingers.count(1)


            cv2.putText(
                img,
                "Fingers: "+str(count),
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,0,0),
                2
            )


            # عرض أسماء الأصابع
            y=100

            for i,state in enumerate(fingers):

                if state:

                    cv2.putText(
                        img,
                        finger_names[i],
                        (20,y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,255,0),
                        2
                    )

                    y+=40



            # رسم نقاط اليد
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )



    cv2.imshow(
        "Hand Finger Recognition",
        img
    )


    # الخروج بزر Q
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()