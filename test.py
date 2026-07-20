import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('mr_turtle.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img / 255.0

img_reshaped = img.reshape((-1, img.shape[2]))
m,n = img_reshaped.shape
print("Shape of the points: ", img_reshaped.shape)
