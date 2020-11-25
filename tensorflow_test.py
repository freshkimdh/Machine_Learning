#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#기존 2.0 버전
#import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

hello = tf.constant("hello, tensorflow")

tf.print(node1, node2)
tf.print(node3)

#1.0 버젼
sess = tf.Session()
print(sess.run(hello))

#2.0 이후 버젼
#tf.print(hello)

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, feed_dict={a:3, b:4.5}))
print(sess.run(adder_node, feed_dict={a:[1,3], b:[2,4]}))

