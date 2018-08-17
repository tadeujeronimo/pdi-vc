import cv2
import numpy as np
import urllib.request as ur
import matplotlib.pyplot as plt

url = 'https://avatars0.githubusercontent.com/u/31942233?s=460&v=4'
url_response = ur.urlopen(url)

img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)

plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

color = ('r','g','b')
for i, col in enumerate(color):
  histr = cv2.calcHist([img], [i], None, [256], [0,256])
  plt.plot(histr,color = col)
  plt.xlim([0, 256])

plt.show()
