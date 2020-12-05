#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# X, Y 값 정의
X = [1,2,3]
Y = [1,2,3]

W = tf.Variable(5.0)

# 가설 정의
#hypothesis = x_train * W + b
hypothesis = X*W

# cost 계산
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최소화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# session 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run(W))
    sess.run(train)
