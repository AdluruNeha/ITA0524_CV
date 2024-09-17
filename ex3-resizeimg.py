import cv2
img = cv2.imread(r"D:\shifted_C\New folder\nature1.jpeg")
smaller_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
larger_img = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Original Image', img)
cv2.imshow('Smaller Image', smaller_img)
cv2.imshow('Larger Image', larger_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
