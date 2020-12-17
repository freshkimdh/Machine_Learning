# 그래프 그리기 위한 lib
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:/Users/user/PycharmProjects/pythonProject2/Level_2_BS_ML/matplot/dog.jpg')


# img = imread('./dog.jpg')

plt.imshow(img)
plt.show()

