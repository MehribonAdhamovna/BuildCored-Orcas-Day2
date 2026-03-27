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
    cap = cv2.VideoCapture(1) 
if not cap.isOpened():
    print("ERROR: No webcam found. Check your camera connection.")
    sys.exit(1)

points = [] # This stores our drawing history
colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255)] # Yellow, Green, Red
colorIndex = 0 # Start with Yellow


while True:
    success, frame = cap.read()
    print("Loop is running!")
    if not success:
                    break

    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)




    cv2.rectangle(frame, (100, 5), (200, 45), (0, 255, 255), -1) # Yellow Box
    cv2.rectangle(frame, (300, 5), (400, 45), (0, 255, 0), -1)   # Green Box
    cv2.rectangle(frame, (500, 5), (600, 45), (0, 0, 255), -1)   # Red Box
   
    if results.multi_hand_landmarks:
    
            for hand_lms in results.multi_hand_landmarks:
        
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
                h, w, c = frame.shape

            
                index_tip = hand_lms.landmark[8]

                
                ix = int(index_tip.x*w) 
                iy = int(index_tip.y*h)

                # COLOR SWITCHER: If hand is in the top header area
            if iy < 50:
                if 100 < ix < 200: colorIndex = 0 # Yellow
                elif 300 < ix < 400: colorIndex = 1 # Green
                elif 500 < ix < 600: colorIndex = 2 # Red

        
            cv2.circle(frame, (ix, iy), 15, (255, 0, 0), -1)

            thumb_tip = hand_lms.landmark[4]

            tx = int(thumb_tip.x*w) 
            ty = int(thumb_tip.y*h)
            
            distance = ((ix - tx)**2 + (iy - ty)**2)**0.5
    
    
            
        # --- THE ONLY DRAWING LOGIC YOU NEED ---
            if distance < 40:
                # 1. Draw a YELLOW circle on the tip (Shows you are clicking)
                cv2.circle(frame, (ix, iy), 15, (0, 255, 255), -1)
                
                # 2. Save the point AND the current color to the list
                points.append(((ix, iy), colors[colorIndex]))
            else:
                # 1. Draw a BLUE circle on the tip (Shows you are moving)
                cv2.circle(frame, (ix, iy), 15, (255, 0, 0), -1)
                
                # 2. Add a break so the line stops
                points.append(None)
    
    
    # Draw the lines with their specific colors
    for i in range(1, len(points)):
        if points[i - 1] is None or points[i] is None:
            continue
        # points[i][0] is the (x,y), points[i][1] is the color
        cv2.line(frame, points[i-1][0], points[i][0], points[i][1], 2)

    cv2.imshow("AirCanvas - Day02", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
    
cap.release()
cv2.destroyAllWindows()
print("\nAirCanvas is done. See you tomorrow for the Day 03!")
