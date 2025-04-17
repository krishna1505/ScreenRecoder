import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Screen dimensions
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

# Video writer setup
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("VideoRecording.mp4", f, 30.0, dim)

# Duration and end time
now_start_time = time.time()
dur = 80  # Duration in seconds (change this to increase recording time)
end_time = now_start_time + dur

while True:
    # Capture screenshot
    image = pyautogui.screenshot()
    frame = np.array(image)
    
    # Since pyautogui returns an RGB image, we convert it to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Write the frame to the video file
    output.write(frame)
    
    # Check if duration has passed
    c_time = time.time()
    if c_time > end_time:
        break

# Release the video writer
output.release()
print("____END___")
