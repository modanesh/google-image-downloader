import os
import cv2

path = "/Users/Mohamad/Projects/Python/google-image-downloader/images/cars/"
i = 0
for filename in os.listdir(path):
    # if filename.endswith(".jpeg"):
    newname = "car" + str(i) + ".jpeg"
    print(newname)
    os.rename(path+filename, path+newname)
    i += 1