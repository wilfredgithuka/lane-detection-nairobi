#WilfedGithuka
#Githuka.com
#ThikaRoad Lane Detection
#Grayscale + Gausian Smoothing + Canny Edge Detector + Region of Interest

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os
import random
#%matplotlib inline

# Everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
from IPython.display import display, HTML
import math

# Helper Functions
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gaussian(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def canny(image, low_threshold, high_threshold):
    return cv2.Canny(image, low_threshold, high_threshold)

def roi(image, region):
    #defining a blank mask to start with
    mask = np.zeros_like(image)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(image.shape) > 2:
        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, region, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def drawLine(image, x, y, color=[255, 0, 0], thickness=20):
    """
    Adjust a line to the points [`x`, `y`] and draws it on the image `img` using `color` and `thickness` for the line.
    """
    if len(x) == 0: 
        return
    
    lineParameters = np.polyfit(x, y, 1) 
    
    m = lineParameters[0]
    b = lineParameters[1]
    
    maxY = image.shape[0]
    maxX = image.shape[1]
    y1 = maxY
    x1 = int((y1 - b)/m)
    y2 = int((maxY/2)) + 60
    x2 = int((y2 - b)/m)
    cv2.line(image, (x1, y1), (x2, y2), [255, 0, 0], 4)

def draw_lines(image, lines, color=[255, 0, 0], thickness=20):
    
    leftPointsX = []
    leftPointsY = []
    rightPointsX = []
    rightPointsY = []

    for line in lines:
        for x1,y1,x2,y2 in line:
            m = (y1 - y2)/(x1 - x2)
            if m < 0:
                leftPointsX.append(x1)
                leftPointsY.append(y1)
                leftPointsX.append(x2)
                leftPointsY.append(y2)
            else:
                rightPointsX.append(x1)
                rightPointsY.append(y1)
                rightPointsX.append(x2)
                rightPointsY.append(y2)

    drawLine(image, leftPointsX, leftPointsY, color, thickness)
        
    drawLine(image, rightPointsX, rightPointsY, color, thickness)

def hough(image, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(image, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    draw_lines(line_image, lines)
    return line_image

def weighted_image(image, initial_image, α=0.8, β=1., λ=0.):
    """
    `image` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_image` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_image * α + img * β + λ
    NOTE: initial_image and iamge must be the same shape!
    """
    return cv2.addWeighted(initial_image, α, image, β, λ)

ColorImage = cv2.imread('RGBImageInput.jpg')
kernel_size = 15
low_threshold = 20
high_threshold = 100

image = grayscale(ColorImage)
gaussian_blurred = gaussian(image, kernel_size)
canny_image = canny(gaussian_blurred, low_threshold, high_threshold)

rho = 1 # distance resolution in pixels of the Hough grid
theta = np.pi/180 # angular resolution in radians of the Hough grid
threshold = 10     # minimum number of votes (intersections in Hough grid cell)
min_line_length = 20 #minimum number of pixels making up a line
max_line_gap = 1    # maximum gap in pixels between connectable line segments

ysize = canny_image.shape[0]
xsize = canny_image.shape[1]
region = np.array([ [0, ysize], [xsize/2,(ysize/2)+ 10], [xsize,ysize] ], np.int32)
# region = np.array([[(100, ysize), (max_width -100, ysize), (max_width/2 + width_delta, ysize/2 + 50), (max_width/2 - width_delta, ysize/2 + 50)]], np.int32)
roi_image = roi(canny_image, [region])

hough_image = hough(roi_image, rho, theta, threshold, min_line_length, max_line_gap)

MergeImage = weighted_image(hough_image, ColorImage)

cv2.imwrite ('GrayImageOutput.jpg', image)
cv2.imwrite ('BluurImageOutput.jpg', gaussian_blurred)
cv2.imwrite ('CannyImageOutput.jpg', canny_image)
cv2.imwrite ('ROIImageOutput.jpg', roi_image)
cv2.imwrite ('HoughImageOutput.jpg', hough_image)
cv2.imwrite ('MergedImageOutput.jpg', MergeImage)
#cv2.imshow ('gray_image', gray_image)
