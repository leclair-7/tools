import cv2
import numpy as np

import datetime

time_stamp = datetime.datetime.now()
time_stamp_str = time_stamp.strftime("%Y-%m-%d_%H-%M-%S")

cap = cv2.VideoCapture(0)

# H264 and xvid didn't work
vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("videos/" + time_stamp_str + ".mp4", vid_cod, 20.0, (640,480))

width  = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("webcam image size:", width, height)

should_run = True
while should_run:
    ret, color_frame_bgr = cap.read()
    
    cv2.imshow('frame', color_frame_bgr)
    output.write(color_frame_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        should_run = False 

# When everything done, release the capture
cap.release()
output.release()

cv2.destroyAllWindows()

