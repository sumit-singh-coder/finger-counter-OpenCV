import cv2
import mediapipe as mp
import os
import pyautogui
video_cap = cv2.VideoCapture(0)


mphands = mp.solutions.hands
hands = mphands.Hands()
draw = mp.solutions.drawing_utils


while True:
    ret , frame = video_cap.read()
    frame = cv2.flip(frame , 1)
    
    imgRGB = cv2.cvtColor(frame  , cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            draw.draw_landmarks(frame , handlms , mphands.HAND_CONNECTIONS)
            index_tip_up = handlms.landmark[8].y <handlms.landmark[6].y 
            thumb_tip_up = handlms.landmark[4].y < handlms.landmark[3].y
            mid_fing_tip = handlms.landmark[12].y < handlms.landmark[10].y
            ring_finger_up = handlms.landmark[16].y < handlms.landmark[14].y
            pinky_finger_up = handlms.landmark[20].y < handlms.landmark[18].y
            
            lm = handlms.landmark
           
            
        

            if index_tip_up and  mid_fing_tip and ring_finger_up and pinky_finger_up and thumb_tip_up:
                 cv2.putText(frame , "5 figer detected" , (20,70) , 1 ,2 , (0,255,0) , 3)     
                 
                      
            elif index_tip_up and  mid_fing_tip and ring_finger_up and pinky_finger_up:
                cv2.putText(frame , "4 figer detected" , (20,70) , 1 ,2 , (0,255,0) , 3)
            elif index_tip_up and  mid_fing_tip and ring_finger_up:
                   cv2.putText(frame , "3 figer detected" , (20,70) , 1 ,2 , (0,255,0) , 3)
            elif index_tip_up and mid_fing_tip:
               
                cv2.putText(frame , "2 figer detected" , (20,70) , 1 ,2 , (0,255,0) , 3)
            elif index_tip_up:
                cv2.putText(frame , "index finger" , (20,70) , 1 ,2 , (0,255,0) , 3)
                
            else:
                    cv2.putText(frame , "fist" , (20,70) , 1 ,2 , (0,255,0) , 3)
                    
                             
           
            

    cv2.imshow("video" , frame)
    if cv2.waitKey(1) == ord("s"):
        break
video_cap.release()    
 