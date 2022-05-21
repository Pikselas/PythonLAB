from matplotlib.cm import get_cmap
from skimage.exposure import equalize_hist
import matplotlib.pyplot as plt


img = plt.imread('dna.jpg')
equalized = equalize_hist(img)

plt.subplot(221)
plt.title("orginal Image")
plt.imshow(img , cmap=get_cmap("gray"))

plt.subplot(222)
plt.title("Histogram")
plt.hist(img.ravel(),256,[0,256])

plt.subplot(223)
plt.title("Equalized Image")
plt.imshow(equalized, cmap=get_cmap("gray"))

plt.subplot(224)
plt.title("Histogram")
plt.hist(equalized.ravel() ,256,[0,256])

plt.show()