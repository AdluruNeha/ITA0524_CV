import cv2
image = cv2.imread(r'D:\shifted_C\New folder\nature1.jpeg')
rotated_image = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow('Original Image', image)
cv2.imshow('Final Rotated Image (180 degrees)', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
