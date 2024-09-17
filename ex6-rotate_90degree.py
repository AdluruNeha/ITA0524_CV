import cv2
image = cv2.imread(r'D:\shifted_C\New folder\nature1.jpeg')
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

flipped_image = cv2.flip(rotated_image, flipCode=0)

cv2.imshow('Original Image', image)

cv2.imshow('Rotated Image', flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
