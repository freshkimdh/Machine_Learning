import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

hello = tf.constant("hello, tensorflow")

tf.print(node1, node2)
tf.print(node3)

#1.0 버젼
#sess = tf.Session()
#print(sess.run(hell0))

#2.0 이후 버젼
tf.print(hello)