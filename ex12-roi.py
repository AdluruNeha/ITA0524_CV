import cv2
import numpy as np

def modify_roi(image_path, start_x, start_y, width, height, color=(0, 255, 0)):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return
    roi = img[start_y:start_y + height, start_x:start_x + width]
    roi[:] = color 
    cv2.imshow('Modified Image with ROI', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r'D:\shifted_C\New folder\nature1.jpeg' 
start_x = 50  
start_y = 50  
width = 100 
height = 100  
color = (255, 0, 0) 
modify_roi(image_path, start_x, start_y, width, height, color)
