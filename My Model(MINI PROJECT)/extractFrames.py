# Program To Read video
# and Extract Frames
import cv2
from django.conf import settings
import django
import os
import os, shutil
from os.path import splitext, dirname, basename, join

# Function to extract frames
def FrameCapture(path):
    output = "C:\\Users\\gandl\\Downloads\\My Model\\output"
    ext = "jpg"
    for filename in os.listdir(output):
        file_path = os.path.join(output, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    # Path to video file
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        return
    idx = 0
    while cap.isOpened():
        idx += 1
        ret, frame = cap.read()
        if ret:
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == 1:  # Save 0 second frame
                cv2.imwrite(output+"/{}_{}.{}".format("frame", "0000", ext),
                            frame)
            elif idx < cap.get(cv2.CAP_PROP_FPS):
                continue
            else:  # Save frames 1 second at a time
                second = int(cap.get(cv2.CAP_PROP_POS_FRAMES) / idx)
                filled_second = str(second).zfill(4)
                cv2.imwrite(output+"/{}_{}.{}".format("frame", filled_second, ext),
                            frame)
                idx = 0
        else:
            break



# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("C:\\Users\\gandl\\Downloads\\My Model\\videos\\faint7.mp4")
