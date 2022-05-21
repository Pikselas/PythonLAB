import cv2
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt


img = cv2.imread('dna.jpg' , 0)
org_hist = cv2.calcHist([img] , [0] , None , [256] , [0 , 256])
equalized = cv2.equalizeHist(img)
equalized_hist = cv2.calcHist([equalized] , [0] , None , [256] , [0, 256])

plt.subplot(221)
plt.title("orginal Image")
plt.imshow(img , cmap=get_cmap("gray"))

plt.subplot(222)
plt.title("Histogram")
plt.hist(org_hist)

plt.subplot(223)
plt.title("Equalized Image")
plt.imshow(equalized, cmap=get_cmap("gray"))

plt.subplot(224)
plt.title("Histogram")
plt.hist(equalized_hist)

plt.show()