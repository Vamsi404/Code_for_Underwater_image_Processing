import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
#%matplotlib inline
import pandas as pd
from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
from keras.utils import np_utils
from skimage.transform import resize   # for resizing images
from PIL import Image
count = 0
videoFile = "C:\\Users\\dell\\Desktop\\RGHS\\video input\\WhatsApp Video 2022-06-05 at 5.56.56 PM - Copy.mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="frame%d.jpg" % count;
        count+=1
        cv2.imwrite('C:\\Users\\dell\\Desktop\\RGHS\\InputImages\\.jpeg'+str(count)+'.jpeg',frame)
cap.release()
#print ("Done!")
#img = plt.imread('frame0.jpg')   # reading image using its name
#plt.imshow(img)