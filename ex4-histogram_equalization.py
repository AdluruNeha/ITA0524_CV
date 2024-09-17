import cv2
img = cv2.imread(r"D:\shifted_C\New folder\nature1.jpeg",cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
cv2.imshow('image ',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
