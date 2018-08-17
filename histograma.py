import cv2
import numpy as np
import urllib.request as ur
from matplotlib import pyplot as plt

#img = cv2.imread('image.jpg', 0)

url = 'https://avatars0.githubusercontent.com/u/31942233?s=460&v=4'
url_response = ur.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, 0)

cv2.imshow('image', img)

plt.hist(img.ravel(), 256, [0,256]);
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
