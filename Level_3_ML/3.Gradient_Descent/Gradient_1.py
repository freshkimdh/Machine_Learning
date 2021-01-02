#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt

# X, Y 값 정의
X = [1,2,3]
Y = [1,2,3]

W = tf.placeholder(tf.float32)

# 가설 정의
hypothesis = X * W

# cost 계산
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# session 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Variables for plotting cost function
W_val = []
cost_val = []
for i in range(-30, 50):
    feed_W = i * 0.1
    curr_cost, curr_W = sess.run([cost, W], feed_dict={W: feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost)

#Show the cost function
plt.plot(W_val, cost_val)
plt.show()
