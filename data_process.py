# Data Increment Code : 2021 AI Engineering Program
# The number of result image is TOTAL times the amount of input image.
# TOTAL = file_number * 3(optional) * (360/degree)

import os
import cv2 
import numpy as np

class Count:
    """
    Class for just counting.
    """
    value=0
    def activate(self):
        Count.value+=1
        return Count.value
    def reset(self):
        Count.value = 0
    def getValue(self):
        return Count.value

class Path:
    """
    Class for creating file repository path.
    """
    repository = "C:/Users/wsChoe/customDataset/labelImg/data/img/"
    def activate(self):
        count = Count()
        return Path.repository + str(count.activate()) + ".jpg"
    def setRepository(repo):
        Path.repository = str(repo)
    def getRepository(self):
        return Path.repository

# Setting
degree = 45
rotate_num = int(360/degree)
file_path = 'C:/Users/wsChoe/customDataset/labelImg/data/original_img/'
file_names = os.listdir(file_path)
path = Path()
img_height = 770
img_width = 578

# Processing
for file in file_names:
    # Reading image
    file_src = file_path + file
    raw_img = cv2.imread(file_src)
    # Resizing image
    img = cv2.resize(raw_img, dsize=(img_width, img_height), interpolation=cv2.INTER_AREA)
    # Rotating, fliping and, saving
    for i in range(rotate_num):
        num = i + 1 # value for rotating value
        # Rotating images every 5 degrees
        height, width, channel = img.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), num*degree, 1)
        rotate_dst = cv2.warpAffine(img, matrix, (width, height))
        cv2.imwrite(path.activate(),rotate_dst)
        # Fliping image
        # Cosider whether this process is necessary.
        x_dst = cv2.flip(rotate_dst, 0) # x-axis symmetry
        cv2.imwrite(path.activate(),x_dst)
        xy_dst = cv2.flip(rotate_dst,-1) # xy axis symmetry maybe is not necessary.
        cv2.imwrite(path.activate(),xy_dst)
        y_dst = cv2.flip(rotate_dst,1) # y-axis symmetry
        cv2.imwrite(path.activate(),y_dst)
