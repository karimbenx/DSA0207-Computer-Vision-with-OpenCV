import cv2
import numpy as np

# Load the image
image_path = "C:/Users/Merwin S/OneDrive/Pictures/Screenshots/girl.png"
a = cv2.imread(image_path)

# Define the Laplacian kernel
Lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Apply the Laplacian filter to the image
a1 = cv2.filter2D(a, -1, Lap)

# Convert the result to uint8 data type
a2 = cv2.convertScaleAbs(a1)

# Display the Laplacian result
cv2.imshow("Laplacian", a2)
cv2.waitKey(0)

# Define a different Laplacian kernel
lap = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# Apply the second Laplacian filter to the image
a3 = cv2.filter2D(a, -1, lap)

# Convert the result to uint8 data type
a4 = cv2.convertScaleAbs(a3)

# Display the result of the second Laplacian filter
cv2.imshow("Second Laplacian", a4)
cv2.waitKey(0)
cv2.destroyAllWindows()

