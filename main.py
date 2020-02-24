# Importing all necessary libraries
import cv2
import os

filename = "ipman.mp4";
cam = cv2.VideoCapture("./" + filename)
frame_array = []

while (True):
    ret, frame = cam.read()
    if ret:
        height, width, layers = frame.shape
        newHeight = int(3840 * height / width)
        newWidth = int(3840)
        size = (newWidth, newHeight)
        frame = cv2.resize(frame, (newWidth, newHeight), interpolation=cv2.INTER_LINEAR)
        frame_array.append(frame)
    else:
        break

out = cv2.VideoWriter("4k" + filename, cv2.VideoWriter_fourcc(*'MP4V'), 30, size)
for i in range(len(frame_array)):
    out.write(frame_array[i])

out.release()
cam.release()
cv2.destroyAllWindows()