import cv2
path = r"D:\shifted_C\New folder\nature1.jpeg"
img = cv2.imread(path)
bluredimg = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("Original image: ",img)
cv2.imshow("Blured image: ",bluredimg)
cv2.waitKey(0)
cv2.destrayAllWindows()
                 
