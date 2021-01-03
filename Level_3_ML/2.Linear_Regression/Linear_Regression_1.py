#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 2.0 버전
# import tensorflow as tf

# X, Y 값 정의 : x가 1 일때, y는 1
x_train = [1, 2, 3]
y_train = [1, 2, 3]

# W, b 값 정의
# tf.random_normal([shape]) 몇 차원?
W = tf.Variable(tf.random_normal([1]), name='weight') # 텐서플로우가 사용하는 변수 선언 "Variable"
b = tf.Variable(tf.random_normal([1]), name='bias')

# 가설 정의
hypothesis = x_train * W + b

# cost 계산
# reduce_mean 평균 내주는 것
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# 최소화 작업 - GradientDesent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# session 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
    sess.run(train)
    if step % 20 == 0: # 20번에 1번씩 출력 (너무 많으니깐)
        print(step, sess.run(cost), sess.run(W), sess.run(b))

#우리가 x,y 값을 준것
