#1.0 버전으로 변경
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 2.0 버전
# import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

# 그래프의 한 요소야 라고 말해 준다
print("node1:",node1, "node2:",node2)
print("node3:",node3)

# 그래프의 노드를 실행
sess = tf.Session()
print("sess.run(node1, node2):", sess.run([node1, node2]))
print("sess.run(node3):", sess.run(node3))