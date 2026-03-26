import cv2 #type: ignore
import mediapipe as mp #type:ignore
import numpy as np #type:ignore
import sys

# Initialize MediaPipe Hand Landmark Mapping
mp_hands = mp.solutions.hands
hands= mp_hands.Hands()

# Initialize the Drawing tool
mp_draw= mp.solutions.drawing_utils

# Start the Webcam
cap=cv2.VideoCapture(0)

if not cap.isOpened():
    cap = cv2.VideoCapture(1)  # Try second camera index
if not cap.isOpened():
    print("ERROR: No webcam found. Check your camera connection.")
    sys.exit(1)

while True:
    success, frame = cap.read()
    print("Loop is running!")
    if not success:
                    break

    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

   
    if results.multi_hand_landmarks:
    
            for hand_lms in results.multi_hand_landmarks:
        
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
                h, w, c = frame.shape

            
                index_tip = hand_lms.landmark[8]

                
                ix = int(index_tip.x*w) 
                iy = int(index_tip.y*h)

        
            cv2.circle(frame, (ix, iy), 15, (255, 0, 0), -1)

            thumb_tip = hand_lms.landmark[4]

            tx = int(thumb_tip.x*w) 
            ty = int(thumb_tip.y*h)
            
            distance = ((ix - tx)**2 + (iy - ty)**2)**0.5
            
            if distance < 40:
    # Draw a YELLOW circle to show a "Click" is happening
                cv2.circle(frame, (ix, iy), 15, (0, 255, 255), -1)
            else:
    # Keep it BLUE when not clicking
                cv2.circle(frame, (ix, iy), 15, (255, 0, 0), -1)


    cv2.imshow("AirCanvas - Day02", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
    
cap.release()
cv2.destroyAllWindows()
print("\nAirCanvas is done. See you tomorrow for the Day 03!")