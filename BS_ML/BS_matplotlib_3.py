# 그래프 그리기 위한 lib
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:/Users/user/PycharmProjects/pythonProject2/BS_ML/dog.jpg')
# img = imread('./BS_ML/dog.jpg')

plt.imshow(img)
plt.show()

