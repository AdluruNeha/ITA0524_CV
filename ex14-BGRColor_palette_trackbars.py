import cv2
import numpy as np

def nothing(x):
    pass

def bgr_palette():
    # Create a black image
    image = np.zeros((300, 500, 3), np.uint8)
    
    # Create a named window
    cv2.namedWindow('BGR Color Palette')
    
    # Create trackbars for color change
    cv2.createTrackbar('B', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('G', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('R', 'BGR Color Palette', 0, 255, nothing)

    while True:
        # Get current positions of the trackbars
        b = cv2.getTrackbarPos('B', 'BGR Color Palette')
        g = cv2.getTrackbarPos('G', 'BGR Color Palette')
        r = cv2.getTrackbarPos('R', 'BGR Color Palette')
        
        # Update the image color
        image[:] = [b, g, r]
        
        # Display the image
        cv2.imshow('BGR Color Palette', image)
        
        # Break the loop when 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # Destroy all windows
    cv2.destroyAllWindows()

# Call the function to run the BGR color palette
bgr_palette()

