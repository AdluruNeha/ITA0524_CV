import cv2
import numpy as np

def apply_smoothing_filter(image_path, kernel_size):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return

    # Apply averaging filter using cv2.blur() or cv2.filter2D()
    smoothed_img = cv2.blur(img, (kernel_size, kernel_size)) 
    
    # Display the original and smoothed images
    cv2.imshow('Original Image', img)
    cv2.imshow('Smoothed Image', smoothed_img)
    
    # Wait for key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return smoothed_img

image_path = r'D:\shifted_C\New folder\nature1.jpeg'  
kernel_size = 5 
apply_smoothing_filter(image_path, kernel_size)
