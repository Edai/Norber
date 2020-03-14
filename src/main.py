# Importing all necessary libraries
import cv2
import os


def resize_frame(f, s):
    return cv2.resize(f, s, interpolation=cv2.INTER_LINEAR)


frame_array = []
filename = input("Enter the full path of the file : ");
try:
    cam = cv2.VideoCapture(filename)
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(3840), int(3840 * height / width))

    while (True):
        ret, frame = cam.read()
        if ret:
            frame_array.append(resize_frame(frame, size))
        else:
            break

    out = cv2.VideoWriter("4k" + filename, cv2.VideoWriter_fourcc(*'MP4V'), 30, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    cam.release()
    cv2.destroyAllWindows()

except cv2.error as e:
    print("Error: Wrong file path")


except:
    print("Error")