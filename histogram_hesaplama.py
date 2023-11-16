import cv2
import numpy as np
from matplotlib import pyplot as plt

photo = cv2.imread("black_cat.png",0)
cv2.imshow("black_cat",photo)

if photo is not None:
    Hist = np.zeros(256)
    w,h = photo.shape
for i in range (0, w):
    for j in range(0, h):
        a = photo[i,j]
        Hist[a] = Hist[a] + 1

plt.plot(Hist)
plt.show()
cv2.waitKey()