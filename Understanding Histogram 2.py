# Histogram method 2

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('one.jpg',0)

# 3rd argument is image mask, for histogram of full img it is None.
# 4th argument is hist size, representation of bin counts, [ ]...
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()