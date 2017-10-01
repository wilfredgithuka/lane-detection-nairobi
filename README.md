# Lane Detection on Nairobi Roads using OpenCV
## A lane detection algorith applied to Nairobi roads in Kenya

![thumb0002](https://user-images.githubusercontent.com/7964520/31053948-6603cb62-a6b0-11e7-8166-2f7077b048ec.jpg)

The main objective of this project is to find lane lines in video using basic computer vision. The lines on the road show us
where the lanes are and act as a constant reference for where to steer the vehicle. Naturally, one of the first things we would
like to do in developing a self-driving car is to automatically detect lane lines using an algorithm.In this project I have
created a pipeline to detect lane lines in images and videos using Python and OpenCV.

## PyconKe
PyConKe 2017 will be the first in a series of anual gatherings of software developers, techies, business people, startups, learning institutions, students and other organizations and individuals that use or otherwise have an interest/stake in the Python programming language and its ecosystem. This will be the basis of my presentation, so incase you did not manage to attend, just clone this repo and you can find the ppt on my website >> githuka.com

## Pipeline
This repo basically introduces the concept of lane detection on roads from a picture feed. Am not done with the video part but the rest of the code's pipeline should work smoothly.

![rgbimageinput](https://user-images.githubusercontent.com/7964520/31053989-6517f1b4-a6b1-11e7-87ee-aa13f31aecae.jpg)
![grayimageoutput](https://user-images.githubusercontent.com/7964520/31053986-6516aef8-a6b1-11e7-8e9d-24e843c4c3bb.jpg)
![bluurimageoutput](https://user-images.githubusercontent.com/7964520/31053990-6517c8f6-a6b1-11e7-9110-740b11635a1f.jpg)
![cannyimageoutput](https://user-images.githubusercontent.com/7964520/31053987-6516f94e-a6b1-11e7-8256-3594bf09ee51.jpg)
![houghimageoutput](https://user-images.githubusercontent.com/7964520/31053988-6517c7ca-a6b1-11e7-80e0-524cc6e91639.jpg)
![mergedimageoutput](https://user-images.githubusercontent.com/7964520/31053991-65187724-a6b1-11e7-8413-04c6b4646355.jpg)


## Credits
* Base code by UDACITY from whom I learnt how to do this, thanks.
* Sample Video: https://youtu.be/YEfSVrZ04h4
