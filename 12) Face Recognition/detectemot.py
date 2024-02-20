import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# read image
img = cv2.imread('KnownImages/someoneH.jpg')

# call imshow() using plt
plt.imshow(img[:,:,::-1])

# display image
plt.show()
result = DeepFace.analyze(img, actions = ['emotion'])

print(result)
