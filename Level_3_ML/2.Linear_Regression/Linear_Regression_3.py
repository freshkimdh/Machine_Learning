#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 2.0 버전
# import tensorflow as tf

# X, Y 값 정의
# 우리가 직접 값을 주지 않고, 필요할때 컴퓨터에게 값을 줘서 답을 구하는 것
#
X = tf.placeholder(tf.float32, shape=[None]) # none은 아무값이나 들어올 수 있다.
Y = tf.placeholder(tf.float32, shape=[None])


# W, b 값 정의
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# 가설 정의
#hypothesis = x_train * W + b
hypothesis = X * W + b #파라미터 사용

# cost 계산
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최소화 작업
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# session 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

'''
# Fit the line
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
'''

# Fit the line 파라미터 사용
for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
                                         feed_dict={X: [1, 2, 3, 4, 5], Y: [2.1, 3.1, 4.1, 5.1, 6.1]})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)

# Testing our model 컴퓨터에 값 던져주면 훈련시킨 값을 받을 수 있음
print(sess.run(hypothesis, feed_dict={X: [5]})) # X가 5이면, Y는 뭐야?
print(sess.run(hypothesis, feed_dict={X: [2.5]}))
print(sess.run(hypothesis, feed_dict={X: [1.5, 3.5]})) # X 값 2개 줄께, 예측해봐