import sys, os
sys.path.append(os.pardir)
import numpy as np
from Level_2_BS_ML.Mnist.dataset.mnist import load_mnist
from PIL import Image

# 미니배치
# 배치사이즈를 설정해서 임의로 10개 출력

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = True)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(np.random.choice(60000,10))