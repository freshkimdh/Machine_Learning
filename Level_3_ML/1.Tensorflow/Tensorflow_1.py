#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 2.0 버전
# import tensorflow as tf

hello = tf.constant("hello")

sess = tf.Session()

print(sess.run(hello))

