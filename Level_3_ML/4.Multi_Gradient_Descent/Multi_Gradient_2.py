# 변수가 3개 있을때 예측하는 Linear Regression
# Matrix 곱셈을 이용 한다.

#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x_data = [[73., 93., 89.],
          [96., 73., 80.],
          [88., 91., 98.],
          [66., 75., 93.],
          [90., 100., 70.]
          ] # 5 X 3
y_data = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]
          ] # 5 X 1

# placeholder for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# (5X3) * (?X?) = 5X1
# ? = 3X1
W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# hypothesis = x1*w1 + x2*w2 + x3*w3 + b
hypothesis = tf.matmul(X, W) + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                         feed_dict={X: x_data, Y:y_data})
    if step % 10 == 0:
        print(step,"cost:", cost_val, "\nPrediction:\n",hy_val)
