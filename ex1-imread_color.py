import cv2
img = cv2.imread(r"D:\shifted_C\New folder\nature1.jpeg" , cv2.IMREAD_GRAYSCALE)
cv2.imshow('image : ',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
