import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train, t_train), (x_test, t_test) = mnist.load_data()

print(x_train.shape)
print(t_train)

digit = x_train[0]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()