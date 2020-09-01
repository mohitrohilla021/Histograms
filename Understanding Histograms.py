# Histogram method 1

import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = np.zeros((200,200),np.uint8)   # all the pixels are black here.
#cv2.rectangle(img,(0,100),(200,200),(255),-1)
#cv2.rectangle(img,(0,50),(100,100),(127),-1)

img = cv2.imread('one.jpg')  # 0 for gray scale mode

b,g,r = cv2.split(img)

cv2.imshow("BLue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)

# plotting the histograms
# ravel() creates a contiguous flattened array...
# pixel value is taken 256, range variation is [0,256]

#plt.hist(img.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()